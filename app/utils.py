import re

def analyze_text(text):
    issues = []
    risk_score = 0
    text = text.lower()

    if "urgente" in text or "inmediatamente" in text:
        issues.append("Tono urgente detectado.")
        risk_score += 2

    if re.search(r"http[s]?://[^\s]+", text):
        issues.append("Enlace detectado: verifica si es seguro.")
        risk_score += 2

    if "suspendida" in text or "bloqueada" in text:
        issues.append("Referencia a cuentas bloqueadas.")
        risk_score += 1

    if "datos personales" in text:
        issues.append("Solicitud de datos personales detectada.")
        risk_score += 2

    # NUEVAS REGLAS para riesgo medio
    if "actividad inusual" in text or "dispositivo desconocido" in text:
        issues.append("Actividad sospechosa detectada.")
        risk_score += 1

    if "cambiar tu contraseña" in text or "restablecer tu contraseña" in text:
        issues.append("Recomendación de cambio de contraseña.")
        risk_score += 1

    if "verifica tu identidad" in text:
        issues.append("Verificación de identidad solicitada.")
        risk_score += 1

    # Clasificación del riesgo
    if risk_score >= 5:
        risk_level = "🔴 Alto"
    elif risk_score >= 3:
        risk_level = "🟠 Medio"
    else:
        risk_level = "🟢 Bajo"

    return {"risk_level": risk_level, "issues": issues}

