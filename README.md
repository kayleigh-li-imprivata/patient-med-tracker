# Patient Medication Tracker

Fake hospital medication tracking application for testing the Bug Ticket Analyzer for the Imprivata AI Bootcamp.

## Purpose

This is a **synthetic codebase** with intentional bugs designed to test automated bug analysis tools.

## Structure

- `src/medication_tracker/` - Main application code
- `logs/` - Error logs in various industry-standard formats (see below)

## Intentional Bugs & Production Logs

This codebase contains 7 intentional bugs, each with a corresponding **production-grade error log** in a different industry-standard format. These logs are based on real-world documentation (AWS Lambda, Prometheus Alertmanager) and contain **NO artificial hints** - no "Bug #X" comments, no `root_cause` fields, no remediation suggestions. The Bug Ticket Analyzer must parse actual stack traces and infer root causes like it would in a real production environment.

| Bug # | Error Type | Location | Log File | Log Format | Key Features |
|-------|------------|----------|----------|------------|--------------|
| #1 | `DrugInteractionError` | `drug_interactions.py:45` | `error_001_drug_interaction_grafana_loki.log` | **Grafana Loki** (LogQL) | K8s metadata (namespace, pod, container), label-based filtering for modern K8s environments |
| #2 | `ValueError` (should be `InvalidDosageError`) | `medication_service.py:34` | `error_002_invalid_dosage_splunk.log` | **Splunk** (key-value) | Splunk sourcetype, index, host fields; key=value format for enterprise environments |
| #3 | `AttributeError` (null patient) | `schedule_validator.py:23` | `error_003_null_patient_elasticsearch.json` | **Elasticsearch/ELK** (JSON) | @timestamp, dot-notation fields, K8s metadata for ELK Stack |
| #4 | `IndexError` (empty list) | `medication_service.py:56` | `error_004_index_error_cloudwatch.json` | **AWS CloudWatch** (JSON) | CloudWatch log groups/streams, AWS ARNs, ECS task metadata |
| #5 | `ValidationError` (invalid date) | `models.py:78` | `error_005_validation_error_datadog.json` | **Datadog APM** (JSON) | ddtags, trace/span IDs, APM correlation, Datadog-specific fields |
| #6 | `KeyError` (missing medication) | `drug_interactions.py:89` | `error_006_key_error_prometheus.log` | **Prometheus** (Alertmanager) | Metrics (counters, gauges), alert rules, correlated log entries |
| #7 | `TypeError` (wrong argument type) | `schedule_validator.py:67` | `error_007_type_error_syslog_batch.log` | **Syslog** (batch) | RFC 3164 format, **repetitive errors (15+ occurrences)** to test noise filtering |

## Testing the Bug Ticket Analyzer

These logs are designed to test the Bug Ticket Analyzer's ability to:
- Parse multiple log formats (text, JSON, metrics)
- Extract stack traces and line numbers
- Handle different metadata structures
- Filter repetitive errors (batch processing)
- Generate accurate GitHub permalinks
- Provide root cause analysis across different logging platforms

## ⚠️ DISCLAIMER

This code is intentionally buggy and should never be used in a real healthcare setting.
