"""Kafka consumers for patient-consent-service.

One handler per subscribed topic. Handlers are best-effort logging plus
audit — services override this file to implement real cross-domain behavior.
"""
from __future__ import annotations

import logging

from healthcare_common.audit import emit_audit

log = logging.getLogger("patient-consent-service.consumers")


def register(svc) -> None:
    bus = svc.bus

    @bus.on("patient.created")
    def _on_patient_created(envelope: dict) -> None:
        log.info("patient-consent-service: received patient.created id=%s", envelope.get("id"))
        emit_audit(bus, action="consume.patient.created", actor="system:patient-consent-service",
                   target=None, details={"envelope_id": envelope.get("id")})

