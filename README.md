# Tugas 2: Job Queue dengan Celery

Repositori ini berisi implementasi sistem *load balancer* untuk analisis log SIEM dan *ML Alert Triage* menggunakan Celery dan RabbitMQ.

## Struktur File
* `celeryconfig.py`: Konfigurasi broker RabbitMQ dan *task routing*.
* `tasks.py`: Skrip *worker* yang berisi logika komputasi `LONG` dan `SHORT`.
* `producer.py`: Skrip generator data (agen SIEM) yang menembakkan *request* secara asinkron.
* `requirements.txt`: Daftar dependensi pustaka Python.
