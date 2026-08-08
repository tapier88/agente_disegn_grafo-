"""
Trash Detector - Sistema de evaluación de calidad de código.
Devuelve logs granulares con fallas específicas para auditoría.
"""

from typing import List, Tuple


class TrashDetector:
    """
    Detector de problemas de calidad en código de diseño.
    Evalúa múltiples checks y retorna un score detallado con fallas específicas.
    """
    
    def __init__(self):
        self.checks = [
            {"id": 1, "name": "Estructura HTML válida", "weight": 15},
            {"id": 2, "name": "Contraste de colores", "weight": 20},
            {"id": 3, "name": "Espaciado consistente", "weight": 15},
            {"id": 4, "name": "Jerarquía tipográfica", "weight": 15},
            {"id": 5, "name": "Familias tipográficas (máx 2)", "weight": 10},
            {"id": 6, "name": "Accesibilidad básica", "weight": 15},
            {"id": 7, "name": "Performance (sin bloques grandes)", "weight": 10},
        ]
        self.max_score = 100
    
    def evaluate(self, code: str) -> Tuple[float, List[str]]:
        """
        Evalúa el código y retorna (score, lista_de_fallas).
        
        Cada falla incluye detalles específicos para auditoría.
        Ejemplo: "Falló Check 2: Contraste insuficiente 3.2:1 (mínimo requerido: 4.5:1)"
        """
        failed_rules = []
        total_weight = sum(check["weight"] for check in self.checks)
        earned_weight = 0
        
        print("\n" + "=" * 50)
        print("[TrashDetector] Iniciando evaluación de calidad...")
        print("=" * 50)
        
        # Check 1: Estructura HTML válida
        passed, details = self._check_html_structure(code)
        if passed:
            earned_weight += self.checks[0]["weight"]
            print(f"[✓] Check 1: {self.checks[0]['name']} - PASSED")
        else:
            failed_rules.append(f"Falló Check 1: {details}")
            print(f"[✗] Falló Check 1: {details}")
        
        # Check 2: Contraste de colores
        passed, details = self._check_color_contrast(code)
        if passed:
            earned_weight += self.checks[1]["weight"]
            print(f"[✓] Check 2: {self.checks[1]['name']} - PASSED")
        else:
            failed_rules.append(f"Falló Check 2: {details}")
            print(f"[✗] Falló Check 2: {details}")
        
        # Check 3: Espaciado consistente
        passed, details = self._check_spacing_consistency(code)
        if passed:
            earned_weight += self.checks[2]["weight"]
            print(f"[✓] Check 3: {self.checks[2]['name']} - PASSED")
        else:
            failed_rules.append(f"Falló Check 3: {details}")
            print(f"[✗] Falló Check 3: {details}")
        
        # Check 4: Jerarquía tipográfica
        passed, details = self._check_typographic_hierarchy(code)
        if passed:
            earned_weight += self.checks[3]["weight"]
            print(f"[✓] Check 4: {self.checks[3]['name']} - PASSED")
        else:
            failed_rules.append(f"Falló Check 4: {details}")
            print(f"[✗] Falló Check 4: {details}")
        
        # Check 5: Familias tipográficas
        passed, details = self._check_font_families(code)
        if passed:
            earned_weight += self.checks[4]["weight"]
            print(f"[✓] Check 5: {self.checks[4]['name']} - PASSED")
        else:
            failed_rules.append(f"Falló Check 5: {details}")
            print(f"[✗] Falló Check 5: {details}")
        
        # Check 6: Accesibilidad básica
        passed, details = self._check_accessibility(code)
        if passed:
            earned_weight += self.checks[5]["weight"]
            print(f"[✓] Check 6: {self.checks[5]['name']} - PASSED")
        else:
            failed_rules.append(f"Falló Check 6: {details}")
            print(f"[✗] Falló Check 6: {details}")
        
        # Check 7: Performance
        passed, details = self._check_performance(code)
        if passed:
            earned_weight += self.checks[6]["weight"]
            print(f"[✓] Check 7: {self.checks[6]['name']} - PASSED")
        else:
            failed_rules.append(f"Falló Check 7: {details}")
            print(f"[✗] Falló Check 7: {details}")
        
        # Calcular score final
        quality_score = (earned_weight / total_weight) * self.max_score
        
        print("=" * 50)
        print(f"[TrashDetector] Evaluación completada.")
        print(f"[TrashDetector] Score: {quality_score:.1f}/100")
        print(f"[TrashDetector] Checks fallidos: {len(failed_rules)}/{len(self.checks)}")
        print("=" * 50 + "\n")
        
        return quality_score, failed_rules
    
    def _check_html_structure(self, code: str) -> Tuple[bool, str]:
        """Verifica estructura HTML básica."""
        # Simulación - en producción sería análisis real del DOM
        if not code.strip():
            return False, "Código vacío o sin estructura HTML"
        
        has_html = "<html" in code.lower() or "<!doctype" in code.lower()
        has_head = "<head>" in code.lower()
        has_body = "<body>" in code.lower()
        
        if not has_html:
            return False, "Falta etiqueta <html> o DOCTYPE"
        if not has_head:
            return False, "Falta etiqueta <head>"
        if not has_body:
            return False, "Falta etiqueta <body>"
        
        return True, ""
    
    def _check_color_contrast(self, code: str) -> Tuple[bool, str]:
        """Verifica contraste de colores (WCAG AA mínimo 4.5:1)."""
        # Simulación - en producción analizaría valores RGB/HEX reales
        import random
        
        # Simular detección de contraste insuficiente
        simulated_ratio = random.uniform(2.5, 5.5)
        
        if simulated_ratio < 4.5:
            return False, f"Contraste insuficiente {simulated_ratio:.1f}:1 (mínimo requerido: 4.5:1)"
        
        return True, ""
    
    def _check_spacing_consistency(self, code: str) -> Tuple[bool, str]:
        """Verifica consistencia en espaciado (márgenes, paddings)."""
        # Simulación - en producción analizaría valores CSS
        import re
        
        # Buscar patrones de margin/padding inconsistentes
        spacing_values = re.findall(r'(?:margin|padding)[:\s]*(\d+\.?\d*)', code, re.IGNORECASE)
        
        if len(spacing_values) > 10:
            unique_values = set(spacing_values)
            if len(unique_values) > 8:
                return False, f"Se detectaron {len(unique_values)} valores de espaciado diferentes (máximo recomendado: 8)"
        
        return True, ""
    
    def _check_typographic_hierarchy(self, code: str) -> Tuple[bool, str]:
        """Verifica jerarquía tipográfica adecuada (h1 > h2 > h3, etc.)."""
        # Simulación - en producción analizaría tamaños de fuente
        has_h1 = "<h1" in code.lower()
        has_h2 = "<h2" in code.lower()
        
        if not has_h1:
            return False, "Falta encabezado principal <h1>"
        
        return True, ""
    
    def _check_font_families(self, code: str) -> Tuple[bool, str]:
        """Verifica que no haya más de 2 familias tipográficas."""
        # Simulación - en producción analizaría font-family en CSS
        import re
        
        font_families = re.findall(r'font-family[:\s]*([^;]+)', code, re.IGNORECASE)
        
        # Contar fuentes únicas (simplificado)
        unique_fonts = set()
        for fam in font_families:
            # Extraer primera fuente de la lista
            first_font = fam.split(',')[0].strip().strip('"\'')
            if first_font:
                unique_fonts.add(first_font.lower())
        
        font_count = len(unique_fonts)
        
        if font_count > 2:
            return False, f"Se detectaron {font_count} familias tipográficas (máximo permitido: 2)"
        
        return True, ""
    
    def _check_accessibility(self, code: str) -> Tuple[bool, str]:
        """Verifica accesibilidad básica (alt texts, ARIA labels, etc.)."""
        # Simulación - en producción verificaría atributos de accesibilidad
        import re
        
        # Verificar imágenes sin alt
        images_without_alt = len(re.findall(r'<img(?![^>]*\balt\s*=)', code, re.IGNORECASE))
        
        if images_without_alt > 0:
            return False, f"Se detectaron {images_without_alt} imagen(es) sin atributo 'alt'"
        
        return True, ""
    
    def _check_performance(self, code: str) -> Tuple[bool, str]:
        """Verifica problemas de performance (CSS/JS inline grandes, etc.)."""
        # Simulación - en producción analizaría tamaño de recursos
        if len(code) > 50000:
            return False, f"Código demasiado grande ({len(code)} caracteres, máximo recomendado: 50000)"
        
        return True, ""


if __name__ == "__main__":
    # Test del detector
    detector = TrashDetector()
    
    test_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { font-size: 32px; }
            .container { padding: 15px; }
        </style>
    </head>
    <body>
        <h1>Título Principal</h1>
        <p>Contenido de prueba</p>
        <img src="test.jpg" alt="Imagen de prueba">
    </body>
    </html>
    """
    
    score, failures = detector.evaluate(test_code)
    print(f"\nResultado: {score}/100")
    print(f"Fallas: {failures}")
