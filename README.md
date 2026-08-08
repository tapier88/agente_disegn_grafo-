# WebReDesign-Graph-Agent (AI Design Graph Engine $10k)

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green.svg)](https://langchain-ai.github.io/langgraph/)
[![FastMCP](https://img.shields.io/badge/FastMCP-Enabled-orange.svg)](https://github.com/punkpeye/fastmcp)
[![React](https://img.shields.io/badge/React-18+-61dafb.svg)](https://react.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3+-38b2ac.svg)](https://tailwindcss.com/)

## 🚀 Descripción

**WebReDesign-Graph-Agent** es un agente autónomo de rediseño web de alto valor (**$5,000 - $10,000 USD**) que transforma sitios web obsoletos en experiencias digitales de élite mediante inteligencia artificial avanzada.

### 🔍 ¿Qué hace este sistema?

1. **Inspecciona webs** existentes y analiza su estructura, diseño y accesibilidad
2. **Extrae el ADN visual** del sitio (paleta de colores, tipografías, patrones de diseño)
3. **Aplica escalas tipográficas fluidas anti-plantilla** usando principios de diseño moderno
4. **Diseña con componentes de élite** de las librerías más prestigiosas:
   - 🎨 **React Bits** - Componentes animados de alta gama
   - ✨ **Aceternity UI** - Componentes con efectos visuales impresionantes
   - 🪄 **Magic UI** - Componentes mágicos para landing pages
   - 📜 **Lenis** - Smooth scroll de última generación
5. **Realiza autocrítica visual** mediante un sistema de QA automatizado con 7 checks de calidad
6. **Genera pitchs de venta interactivos** listos para presentar al cliente

### 💰 Modelo de Valor

Este sistema está diseñado para agencias y freelancers que buscan escalar servicios de rediseño web premium:

| Nivel | Score | Valor Estimado | Uso |
|-------|-------|----------------|-----|
| Bronze | 70-79 | $3,000 - $5,000 | Rediseño básico |
| Silver | 80-89 | $5,000 - $8,000 | Rediseño profesional |
| Gold | 90-100 | $8,000 - $10,000+ | Rediseño de élite |

---

## 🏗️ Arquitectura de Nodos (LangGraph)

El sistema implementa un grafo de estado con 6 nodos especializados que trabajan de forma orquestada:

```
┌─────────────────────────────────────────────────────────────────┐
│                    WEBREDESIGN GRAPH FLOW                       │
└─────────────────────────────────────────────────────────────────┘

    ┌──────────────────┐
    │ 1. Scout Lead    │ ──► Analiza URL objetivo y extrae datos iniciales
    │ (scout_lead.py)  │     (tecnología, estructura, problemas visibles)
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │ 2. DNA Extractor │ ──► Extrae ADN visual (colores, fuentes, spacing)
    │ (dna_extractor)  │     Genera informe de identidad visual actual
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │ 3. Typography    │ ──► Aplica escala tipográfica fluida
    │    Engine        │     Fórmula: clamp(min, vw-based, max)
    │ (typography_eng) │     Anti-plantilla: cálculos dinámicos
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │ 4. $10k Redesign │ ──► Genera código con componentes premium
    │    Generator     │     React Bits + Aceternity + Magic UI
    │ (redesign_gen)   │     Integración de Lenis smooth scroll
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐      Score < 85       ┌─────────────────┐
    │ 5. Trash Detector│ ────────────────►     │ Reintentos (×3) │
    │    (QA Gate)     │                       │ + Mejor Iteración│
    │ (trash_detector) │ ◄────────────────    └─────────────────┘
    └────────┬─────────┘      Score ≥ 85
             │
             ▼
    ┌──────────────────┐
    │ 6. Pitch Creator │ ──► Genera presentación de venta
    │    (pitch_creator│     Informe ejecutivo + ROI estimado
    │     .py)         │     Código final + recomendaciones
    └──────────────────┘
```

### Detalle de Nodos

#### 1. Lead Hunter & Scouting (`scout_lead.py`)
- **Responsabilidad**: Analizar la URL objetivo y recopilar información inicial
- **Tecnologías**: Playwright, BeautifulSoup, requests
- **Output**: Datos estructurados del lead (tech stack, problemas detectados, oportunidad)

#### 2. Inspection & Web DNA Extractor (`dna_extractor.py`)
- **Responsabilidad**: Extraer la identidad visual actual del sitio
- **Checks**: Colores principales, tipografías, espaciado, jerarquía
- **Output**: JSON con ADN visual completo

#### 3. Typography Anti-Template Engine (`typography_engine.py`)
- **Responsabilidad**: Calcular escalas tipográficas fluidas personalizadas
- **Fórmula**: `clamp(1rem, 2.5vw, 2.5rem)` adaptada al contenido
- **Output**: Sistema tipográfico completo (h1-h6, body, captions)

#### 4. $10k Redesign Generator (`redesign_generator.py`)
- **Responsabilidad**: Generar código del rediseño con componentes premium
- **Componentes**: React Bits, Aceternity UI, Magic UI, Lenis
- **Output**: Código HTML/React/Tailwind listo para producción

#### 5. Visual QA & Self-Critique Gate (`trash_detector.py`)
- **Responsabilidad**: Evaluar calidad del diseño generado
- **7 Checks de Calidad**:
  1. Estructura HTML válida (15 pts)
  2. Contraste de colores WCAG AA (20 pts)
  3. Espaciado consistente (15 pts)
  4. Jerarquía tipográfica (15 pts)
  5. Máximo 2 familias tipográficas (10 pts)
  6. Accesibilidad básica (15 pts)
  7. Performance (10 pts)
- **Loop de Auto-Mejora**: Hasta 3 reintentos si score < 85
- **Selección Inteligente**: Si se agotan reintentos, selecciona la mejor iteración

#### 6. Pitch & Cold Outreach Creator (`pitch_creator.py`)
- **Responsabilidad**: Generar presentación de venta para el cliente
- **Contenido**: Problemas detectados, solución propuesta, ROI estimado, timeline
- **Output**: Pitch deck interactivo + código final + documentación

---

## 📁 Estructura del Proyecto

```
WebReDesign-Graph-Agent/
├── 📄 README.md                 # Documentación principal
├── 📄 requirements.txt          # Dependencias del proyecto
├── 📄 main.py                   # Punto de entrada principal
├── 📄 .gitignore               # Archivos ignorados por Git
│
├── 📂 core/                     # Núcleo del sistema (LangGraph)
│   ├── __init__.py
│   ├── harness.py              # Orquestador del grafo + control de reintentos
│   └── __pycache__/
│
├── 📂 skills/                   # Habilidades especializadas (nodos del grafo)
│   ├── __init__.py
│   ├── trash_detector.py       # Sistema de evaluación de calidad (QA Gate)
│   ├── scout_lead.py           # [Próximamente] Análisis de leads
│   ├── dna_extractor.py        # [Próximamente] Extracción de ADN visual
│   ├── typography_engine.py    # [Próximamente] Motor tipográfico
│   ├── redesign_generator.py   # [Próximamente] Generador de diseños $10k
│   └── pitch_creator.py        # [Próximamente] Creador de pitches
│   └── __pycache__/
│
├── 📂 outputs/                  # [Opcional] Resultados generados
│   ├── designs/                # Diseños generados
│   ├── pitches/                # Pitches creados
│   └── reports/                # Informes de análisis
│
└── 📂 tests/                    # [Opcional] Tests unitarios y de integración
    ├── test_trash_detector.py
    ├── test_harness.py
    └── test_integration.py
```

---

## 🛠️ Guía de Instalación y Uso

### Requisitos Previos

- **Python 3.11 o superior** ([Descargar](https://www.python.org/downloads/))
- **pip** (gestor de paquetes de Python)
- **Node.js 18+** (opcional, para previsualización de componentes React)
- **Git** (para clonar el repositorio)

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/WebReDesign-Graph-Agent.git
cd WebReDesign-Graph-Agent
```

### Paso 2: Instalar Dependencias

```bash
# Crear entorno virtual recomendado
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 3: Instalar Playwright (navegador headless)

```bash
playwright install
playwright install-deps  # Solo Linux, instala dependencias del sistema
```

### Paso 4: Ejecutar el Sistema

```bash
# Ejecución básica (usa configuración por defecto)
python main.py

# Ejecución con URL específica (próximamente)
python main.py --url https://ejemplo.com

# Ejecución con modo debug
python main.py --debug
```

### Paso 5: Ver Resultados

El sistema generará output en consola con:
- ✅ Score de calidad del diseño (0-100)
- 📋 Historial completo de intentos
- 🏆 Mejor iteración seleccionada
- 📊 Detalles de reglas fallidas (si aplica)
- 💼 Pitch de venta generado

---

## ⚙️ Configuración Avanzada

### Variables de Entorno (Opcional)

Crea un archivo `.env` en la raíz del proyecto:

```bash
# API Keys (cuando se integren LLMs externos)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# Configuración del sistema
DEBUG_MODE=true
MAX_RETRIES=3
MIN_SCORE_THRESHOLD=85
OUTPUT_DIR=./outputs
```

### Parámetros Ajustables

En `core/harness.py`:

```python
# Límite de reintentos (default: 3)
MAX_RETRIES = 3

# Score mínimo para aprobar (default: 85)
MIN_SCORE_THRESHOLD = 85

# Límite de recursión del grafo (default: 50)
config = {"recursion_limit": 50}
```

---

## 🧪 Testing

### Ejecutar Tests Unitarios

```bash
# Instalar pytest si no está instalado
pip install pytest

# Ejecutar todos los tests
pytest tests/

# Ejecutar tests con verbose
pytest tests/ -v

# Ejecutar tests con coverage
pytest tests/ --cov=.
```

### Test Rápido del Trash Detector

```bash
python skills/trash_detector.py
```

---

## 📊 Ejemplo de Output

```
======================================================================
  SISTEMA DE REDISEÑO AUTOMÁTICO CON LANGGRAPH - FASE 4
  Fix definitivo: GraphRecursionError + Retención de mejor iteración
======================================================================

============================================================
[Harness] Iniciando proceso de rediseño...
============================================================
[Harness] Generando rediseño (Intento 1)
[Harness] Reglas fallidas anteriores: []

==================================================
[TrashDetector] Iniciando evaluación de calidad...
==================================================
[✓] Check 1: Estructura HTML válida - PASSED
[✗] Falló Check 2: Contraste insuficiente 3.2:1 (mínimo requerido: 4.5:1)
[✓] Check 3: Espaciado consistente - PASSED
[✗] Falló Check 4: Falta encabezado principal <h1>
[✓] Check 5: Familias tipográficas (máx 2) - PASSED
[✗] Falló Check 6: Se detectaron 3 imagen(es) sin atributo 'alt'
[✓] Check 7: Performance - PASSED
==================================================
[TrashDetector] Evaluación completada.
[TrashDetector] Score: 65.0/100
[TrashDetector] Checks fallidos: 3/7
==================================================

[Router] Score 65.0 < 85. Reintentos disponibles (1/3). Regenerando...

... (proceso se repite hasta alcanzar score >= 85 o agotar reintentos)

[Harness] Reintentos agotados. Seleccionando la mejor iteración 
(Intento 2 con Score 78.5/100). Avanzando a Pitch Creator.

======================================================================
  RESULTADOS FINALES
======================================================================

✓ Score Final: 78.5/100
✓ Total de Intentos: 3
✓ Resumen: Diseño optimizado con score 78.5/100

📋 Historial de Intentos:
----------------------------------------------------------------------
  Intento #1: Score 65.0/100
    Fallas: 3 reglas
  Intento #2: Score 78.5/100
    Fallas: 2 reglas
  Intento #3: Score 72.0/100
    Fallas: 3 reglas
----------------------------------------------------------------------
🏆 Mejor Iteración: Intento #2 (Score: 78.5/100)
======================================================================
```

---

## 🔄 Flujo de Trabajo Típico

1. **Input**: URL del sitio web del cliente
2. **Scouting**: Análisis automático de tecnología y estructura
3. **DNA Extraction**: Extracción de identidad visual actual
4. **Typography**: Aplicación de escala tipográfica fluida
5. **Redesign**: Generación de diseño con componentes premium
6. **QA Loop**: Evaluación y auto-mejora (hasta 3 iteraciones)
7. **Pitch Generation**: Creación de presentación de venta
8. **Output**: Diseño final + Pitch deck + Documentación

---

## 🚧 Roadmap

### ✅ Fase 4 (Completada)
- [x] Control de reintentos en LangGraph
- [x] Selección de la mejor iteración
- [x] Logs granulares en Trash Detector
- [x] Configuración de recursion_limit
- [x] Documentación completa del proyecto

### 🔜 Fase 5 (Próximamente)
- [ ] Implementar nodo `scout_lead.py`
- [ ] Implementar nodo `dna_extractor.py`
- [ ] Implementar nodo `typography_engine.py`
- [ ] Implementar nodo `redesign_generator.py`
- [ ] Implementar nodo `pitch_creator.py`

### 🎯 Fase 6 (Futuro)
- [ ] Integración con APIs de LLM (OpenAI, Anthropic)
- [ ] Interfaz web para visualización de resultados
- [ ] Exportación a múltiples formatos (React, Vue, Svelte)
- [ ] Sistema de plugins para componentes personalizados

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está licenciado bajo la MIT License - ver el archivo [LICENSE](LICENSE) para detalles.

---

## 👨‍💻 Autor

Desarrollado como parte del sistema **AI Design Graph Engine** para agencias y freelancers de diseño web premium.

---

## 📞 Soporte

Para issues, preguntas o sugerencias:
- 🐛 Reporta bugs en la sección [Issues](https://github.com/tu-usuario/WebReDesign-Graph-Agent/issues)
- 💬 Discusiones en [Discussions](https://github.com/tu-usuario/WebReDesign-Graph-Agent/discussions)
- 📧 Email: tu-email@ejemplo.com

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella! ⭐**

Hecho con ❤️ para la comunidad de desarrolladores y diseñadores web

</div>
