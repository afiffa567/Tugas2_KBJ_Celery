from celery import Celery
import time
import json
import celeryconfig

# Inisialisasi aplikasi Celery dan memuat konfigurasi
app = Celery("siem_celery")
app.config_from_object('celeryconfig')

@app.task(bind=True)
def process_ml_triage(self, payload):
    """
    Task LONG: Analisis Machine Learning untuk Alert Triage
    Akan dirutekan otomatis ke queue 'q_long_computation'
    """
    time.sleep(3) # Simulasi komputasi model ML
    try:
        data = json.loads(payload)
        risk_score = 95 if data.get("attack_type") in ["SQLi", "DoS"] else 30
        return f"TRIAGE OK: Agent {data.get('agent_name')} | Risk: {risk_score}%"
    except Exception as e:
        return f"TRIAGE FAIL: {e}"

@app.task(bind=True)
def process_wazuh_ping(self, payload):
    """
    Task SHORT: Pengecekan status ketersediaan agen (Health-check)
    Akan dirutekan otomatis ke queue 'q_short_computation'
    """
    try:
        data = json.loads(payload)
        return f"PING OK: Agent {data.get('agent_id')} Active"
    except Exception:
        return "PING OK: Agent Active"
