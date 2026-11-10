import json
import time
from tasks import process_ml_triage, process_wazuh_ping

def generate_siem_traffic():
    print("=== SIEM Log Generator (Producer) Memulai Transmisi ===")
    
    # Simulasi 5 antrean log beruntun
    log_events = [
        {"type": "ping", "data": {"agent_id": "WAF-Node-01", "status": "active"}},
        {"type": "triage", "data": {"agent_name": "Web-App", "attack_type": "SQLi"}},
        {"type": "ping", "data": {"agent_id": "WAF-Node-02", "status": "active"}},
        {"type": "triage", "data": {"agent_name": "DB-Core", "attack_type": "DoS"}},
        {"type": "ping", "data": {"agent_id": "WAF-Node-03", "status": "active"}}
    ]
    
    async_results = []
    
    for event in log_events:
        payload_str = json.dumps(event["data"])
        
        # Klien membuat task yang dikirim ke RabbitMQ secara asynchronous
        if event["type"] == "ping":
            print(f"[Producer] Mengirim SHORT Task (Ping) -> {payload_str}")
            # Pemanggilan delay() melempar pesan ke antrean broker
            res = process_wazuh_ping.delay(payload_str)
        else:
            print(f"[Producer] Mengirim LONG Task (ML Triage) -> {payload_str}")
            res = process_ml_triage.delay(payload_str)
            
        async_results.append(res)
        time.sleep(0.5)
        
    print("\n[Producer] Seluruh pesan telah dikirim ke Broker.")
    print("[Producer] Menunggu hasil dari Worker...\n")
    
    # Menarik hasil dari result backend
    for res in async_results:
        # get() akan memblokir hingga worker selesai memproses pesan terkait
        final_output = res.get()
        print(f"Hasil Eksekusi Worker: {final_output}")

if __name__ == "__main__":
    generate_siem_traffic()
