"""
Core Harness - Orquestador del sistema de rediseño con LangGraph.
Implementa control de reintentos y selección de la mejor iteración.
"""

from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, END


class AgentState(TypedDict, total=False):
    """Estado del agente con historial de intentos."""
    # Estado actual del diseño
    current_code: str
    quality_score: float
    failed_rules: List[str]
    
    # Contador de reintentos
    retry_count: int
    
    # Historial de todos los intentos realizados
    attempt_history: List[Dict[str, Any]]
    
    # Datos para el pitch final
    pitch_data: Optional[Dict[str, Any]]
    
    # Snapshot del estado para restauración
    state_snapshot: Optional[Dict[str, Any]]


def redesign_generator_node(state: AgentState) -> AgentState:
    """
    Nodo generador de rediseños.
    Genera una nueva versión del código basada en el feedback anterior.
    """
    retry_count = state.get("retry_count", 0)
    failed_rules = state.get("failed_rules", [])
    
    print(f"[Harness] Generando rediseño (Intento {retry_count + 1})")
    print(f"[Harness] Reglas fallidas anteriores: {failed_rules}")
    
    # Simulación de generación de código (en producción esto llamaría al LLM)
    # El código real sería generado por un modelo LLM basado en las reglas fallidas
    generated_code = f"// Rediseño Iteración {retry_count + 1}\n"
    generated_code += "// Código optimizado basado en feedback anterior\n"
    generated_code += "const design = { /* ... */ };\n"
    
    return {
        "current_code": generated_code,
        "retry_count": retry_count + 1
    }


def trash_detector_node(state: AgentState) -> AgentState:
    """
    Nodo detector de problemas de calidad (Trash Detector).
    Evalúa el código generado y asigna un score de calidad.
    """
    from skills.trash_detector import TrashDetector
    
    current_code = state.get("current_code", "")
    retry_count = state.get("retry_count", 1)
    
    print(f"[Harness] Evaluando calidad del intento {retry_count}...")
    
    # Instanciar detector y evaluar
    detector = TrashDetector()
    quality_score, failed_rules = detector.evaluate(current_code)
    
    print(f"[Harness] Score obtenido: {quality_score}/100")
    print(f"[Harness] Reglas fallidas: {failed_rules}")
    
    # Crear snapshot del estado actual
    state_snapshot = {
        "current_code": current_code,
        "quality_score": quality_score,
        "failed_rules": failed_rules.copy() if failed_rules else [],
        "retry_count": retry_count
    }
    
    # Registrar este intento en el historial
    attempt_record = {
        "attempt": retry_count,
        "score": quality_score,
        "code": current_code,
        "feedback": failed_rules,
        "state_snapshot": state_snapshot
    }
    
    # Obtener historial existente o crear uno nuevo
    attempt_history = state.get("attempt_history", [])
    attempt_history.append(attempt_record)
    
    return {
        "quality_score": quality_score,
        "failed_rules": failed_rules,
        "attempt_history": attempt_history,
        "state_snapshot": state_snapshot
    }


def pitch_creator_node(state: AgentState) -> AgentState:
    """
    Nodo creador del pitch final.
    Genera la presentación del mejor diseño seleccionado.
    
    Si se restauró un intento previo (cuando se agotaron los reintentos),
    usa los datos del mejor intento en lugar del último.
    """
    # Verificar si hay información del mejor intento restaurado
    best_attempt_info = state.get("best_attempt_info")
    
    if best_attempt_info:
        # Usar los datos del mejor intento restaurado
        current_code = state.get("current_code", "")
        quality_score = best_attempt_info.get("score", 0)
        print(f"[PitchCreator] Usando código del mejor intento #{best_attempt_info.get('attempt')} restaurado (Score: {quality_score}/100)")
    else:
        # Usar el estado actual normal
        current_code = state.get("current_code", "")
        quality_score = state.get("quality_score", 0)
    
    retry_count = state.get("retry_count", 1)
    
    print(f"[Harness] Generando pitch final con score {quality_score}/100")
    print(f"[Harness] Proceso completado en {retry_count} intento(s)")
    
    # Simulación de creación del pitch (en producción esto sería más elaborado)
    pitch_data = {
        "final_code": current_code,
        "final_score": quality_score,
        "total_attempts": retry_count,
        "summary": f"Diseño optimizado con score {quality_score}/100"
    }
    
    return {
        "pitch_data": pitch_data
    }


def router_edge(state: AgentState) -> str:
    """
    Enrutador condicional que decide el flujo del grafo.
    
    Lógica:
    - Si quality_score >= 85 -> Enruta a pitch_creator_node
    - Si quality_score < 85 Y retry_count < 3 -> Re-enruta a redesign_generator_node
    - Si retry_count >= 3 -> Selecciona el mejor intento y enruta a pitch_creator_node
    
    Nota: Las modificaciones al estado para restaurar el mejor intento se hacen 
    directamente en el state dictionary antes de retornar, asegurando que el 
    siguiente nodo reciba los datos correctos.
    """
    quality_score = state.get("quality_score", 0)
    retry_count = state.get("retry_count", 0)
    attempt_history = state.get("attempt_history", [])
    
    print(f"[Router] Evaluando ruta: score={quality_score}, retries={retry_count}")
    
    # Caso 1: Score suficiente -> Avanzar a Pitch Creator
    if quality_score >= 85:
        print(f"[Router] Score {quality_score} >= 85. Avanzando a Pitch Creator.")
        return "pitch_creator_node"
    
    # Caso 2: Score insuficiente pero hay reintentos disponibles
    if retry_count < 3:
        print(f"[Router] Score {quality_score} < 85. Reintentos disponibles ({retry_count}/3). Regenerando...")
        return "redesign_generator_node"
    
    # Caso 3: Reintentos agotados -> Seleccionar el mejor intento
    print(f"[Router] Reintentos agotados ({retry_count}/3). Buscando mejor iteración...")
    
    if attempt_history:
        # Encontrar el intento con el score más alto
        best_attempt = max(attempt_history, key=lambda x: x.get("score", 0))
        
        log_msg = f"[Harness] Reintentos agotados. Seleccionando la mejor iteración (Intento {best_attempt['attempt']} con Score {best_attempt['score']}/100). Avanzando a Pitch Creator."
        print(log_msg)
        
        # Restaurar el estado del mejor intento - MODIFICANDO EL ESTADO DIRECTAMENTE
        best_code = best_attempt.get("code", "")
        best_score = best_attempt.get("score", 0)
        best_feedback = best_attempt.get("feedback", [])
        
        # Actualizar el estado con el mejor intento
        state["current_code"] = best_code
        state["quality_score"] = best_score
        state["failed_rules"] = best_feedback
        
        # Guardar información del mejor intento para que pitch_creator_node la use
        state["best_attempt_info"] = {
            "attempt": best_attempt['attempt'],
            "score": best_attempt['score']
        }
        
        print(f"[Harness] Estado restaurado al Intento {best_attempt['attempt']} (Score: {best_score}/100)")
    
    return "pitch_creator_node"


def build_graph() -> StateGraph:
    """
    Construye y retorna el grafo compilado.
    """
    # Crear el grafo con el estado definido
    workflow = StateGraph(AgentState)
    
    # Añadir nodos
    workflow.add_node("redesign_generator_node", redesign_generator_node)
    workflow.add_node("trash_detector_node", trash_detector_node)
    workflow.add_node("pitch_creator_node", pitch_creator_node)
    
    # Definir punto de entrada
    workflow.set_entry_point("redesign_generator_node")
    
    # Añadir edges condicionales usando la sintaxis correcta de LangGraph
    workflow.add_conditional_edges(
        source="redesign_generator_node",
        path=router_edge,
        path_map={
            "redesign_generator_node": "trash_detector_node",
            "pitch_creator_node": "pitch_creator_node"
        }
    )
    
    workflow.add_conditional_edges(
        source="trash_detector_node",
        path=router_edge,
        path_map={
            "redesign_generator_node": "redesign_generator_node",
            "pitch_creator_node": "pitch_creator_node"
        }
    )
    
    # Edge final desde pitch_creator_node
    workflow.add_edge("pitch_creator_node", END)
    
    # Compilar el grafo
    app = workflow.compile()
    
    return app


async def run_harness(initial_state: Optional[AgentState] = None) -> AgentState:
    """
    Ejecuta el harness completo.
    """
    app = build_graph()
    
    # Estado inicial por defecto
    if initial_state is None:
        initial_state = {
            "current_code": "",
            "quality_score": 0,
            "failed_rules": [],
            "retry_count": 0,
            "attempt_history": []
        }
    
    # Configuración con límite de recursión
    config = {"recursion_limit": 50}
    
    print("=" * 60)
    print("[Harness] Iniciando proceso de rediseño...")
    print("=" * 60)
    
    final_state = await app.ainvoke(initial_state, config=config)
    
    print("=" * 60)
    print("[Harness] Proceso completado exitosamente!")
    print(f"[Harness] Score final: {final_state.get('quality_score', 0)}/100")
    print(f"[Harness] Total de intentos: {final_state.get('retry_count', 0)}")
    print("=" * 60)
    
    return final_state


if __name__ == "__main__":
    import asyncio
    
    async def main():
        result = await run_harness()
        print("\nResultado final:")
        print(f"Código: {result.get('current_code', '')[:100]}...")
        print(f"Score: {result.get('quality_score', 0)}/100")
        print(f"Pitch Data: {result.get('pitch_data', {})}")
    
    asyncio.run(main())
