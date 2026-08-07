# patient-consent-service

patient-consent-service — domain: patients

- **Port:** 8102
- **Language:** Python 3.11 + Flask
- **Database:** `patients` (Postgres, table `patient_consent`)
- **Event bus:** Kafka

## API

| Method    | Path                       |
|-----------|----------------------------|
| GET       | `/api/patient_consent/`          |
| POST      | `/api/patient_consent/`          |
| GET       | `/api/patient_consent/<id>`      |
| PUT/PATCH | `/api/patient_consent/<id>`      |
| DELETE    | `/api/patient_consent/<id>`      |
| GET       | `/health`                  |
| GET       | `/ready`                   |

## Events

**Publishes:** patient.consent.updated
**Subscribes:** patient.created

## HTTP peer dependencies

- `patients-service`
- `audit-log-service`

## Local dev

```bash
pip install -e ../../libs/py-healthcare-common
pip install -r requirements.txt
cp .env.example .env
(cd ../../infra && docker compose up -d postgres kafka kafka-init)
python -m app.main
```

## Tests

```bash
pytest
```
