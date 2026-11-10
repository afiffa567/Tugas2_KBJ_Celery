broker_url = 'amqp://guest:guest@localhost:5672//'
result_backend = 'rpc://'

# Task Routing: Spesifikasi destinasi antrean (queue)
task_routes = {
    'tasks.process_ml_triage': {'queue': 'q_long_computation'},
    'tasks.process_wazuh_ping': {'queue': 'q_short_computation'},
}
