
import re

def analyze_text(text):
    issues = []
    risk_score = 0

    # Reglas simples de ejemplo
    if "urgente" in text.lower() or "inmediatamente" in text.lower():
        issues.append("Tono urgente detectado.")
        risk_score += 2

    if re.search(r"http[s]?://[^\s]+", text):
        issues.append("Enlace detectado: verifica si es seguro.")
        risk_score += 2

    if "suspendida" in text.lower() or "bloqueada" in text.lower():
        issues.append("Referencia a cuentas bloqueadas.")
        risk_score += 1

    if "datos personales" in text.lower():
        issues.append("Solicitud de datos personales detectada.")
        risk_score += 2

    # Clasificación básica del riesgo
    if risk_score >= 5:
        risk_level = "🔴 Alto"
    elif risk_score >= 3:
        risk_level = "🟠 Medio"
    else:
        risk_level = "🟢 Bajo"

    return {"risk_level": risk_level, "issues": issues}
