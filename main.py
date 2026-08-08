"""
Main - Punto de entrada principal del sistema.
Configura y ejecuta el grafo LangGraph con límites de recursión apropiados.
"""

import asyncio
from typing import Dict, Any, Optional
from core.harness import run_harness, AgentState


async def main():
    """
    Función principal que inicializa y ejecuta el sistema de rediseño.
    """
    print("\n" + "=" * 70)
    print("  SISTEMA DE REDISEÑO AUTOMÁTICO CON LANGGRAPH - FASE 4")
    print("  Fix definitivo: GraphRecursionError + Retención de mejor iteración")
    print("=" * 70 + "\n")
    
    # Estado inicial opcional (puede ser None para usar defaults)
    initial_state: Optional[AgentState] = {
        "current_code": "",
        "quality_score": 0,
        "failed_rules": [],
        "retry_count": 0,
        "attempt_history": []
    }
    
    try:
        # Ejecutar el harness con configuración de recursión
        final_state = await run_harness(initial_state)
        
        # Mostrar resultados finales
        print("\n" + "=" * 70)
        print("  RESULTADOS FINALES")
        print("=" * 70)
        
        pitch_data = final_state.get("pitch_data", {})
        print(f"\n✓ Score Final: {pitch_data.get('final_score', 0):.1f}/100")
        print(f"✓ Total de Intentos: {pitch_data.get('total_attempts', 0)}")
        print(f"✓ Resumen: {pitch_data.get('summary', 'N/A')}")
        
        # Mostrar historial completo de intentos
        attempt_history = final_state.get("attempt_history", [])
        if attempt_history:
            print("\n📋 Historial de Intentos:")
            print("-" * 70)
            for attempt in attempt_history:
                print(f"  Intento #{attempt['attempt']}: Score {attempt['score']:.1f}/100")
                if attempt.get('feedback'):
                    print(f"    Fallas: {len(attempt['feedback'])} reglas")
            
            # Identificar el mejor intento
            best_attempt = max(attempt_history, key=lambda x: x.get("score", 0))
            print("-" * 70)
            print(f"🏆 Mejor Iteración: Intento #{best_attempt['attempt']} "
                  f"(Score: {best_attempt['score']:.1f}/100)")
        
        print("=" * 70 + "\n")
        
        return final_state
        
    except Exception as e:
        print(f"\n[ERROR] Error durante la ejecución: {str(e)}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
