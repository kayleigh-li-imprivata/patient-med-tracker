# Patient Medication Tracker

Fake hospital medication tracking application for testing the Bug Ticket Analyzer for the Imprivata AI Bootcamp.

## Purpose

This is a **synthetic codebase** with intentional bugs designed to test automated bug analysis tools.

## Structure

- `src/medication_tracker/` - Main application code
- `logs/` - Error logs in various industry-standard formats (see below)

## Intentional Bugs

This codebase contains 7 intentional bugs, each with a corresponding log file:

| Bug # | Error Type | Location | Log File | Log Format |
|-------|------------|----------|----------|------------|
| #1 | `DrugInteractionError` | `drug_interactions.py:45` | `error_001_drug_interaction_grafana_loki.log` | Grafana Loki (LogQL) |
| #2 | `ValueError` (should be `InvalidDosageError`) | `medication_service.py:34` | `error_002_invalid_dosage_splunk.log` | Splunk |
| #3 | `AttributeError` (null patient) | `schedule_validator.py:23` | `error_003_null_patient_elasticsearch.json` | Elasticsearch/ELK |
| #4 | `IndexError` (empty list) | `medication_service.py:56` | `error_004_index_error_cloudwatch.json` | AWS CloudWatch |
| #5 | `ValidationError` (invalid date) | `models.py:78` | `error_005_validation_error_datadog.json` | Datadog APM |
| #6 | `KeyError` (missing medication) | `drug_interactions.py:89` | `error_006_key_error_prometheus.log` | Prometheus |
| #7 | `TypeError` (wrong argument type) | `schedule_validator.py:67` | `error_007_type_error_syslog_batch.log` | Syslog (batch) |

## Log Files

The `logs/` directory contains **production-grade error logs** in 7 different formats commonly used in enterprise environments. These logs are based on real-world documentation (AWS Lambda, Prometheus Alertmanager) and contain **NO artificial hints** - no "Bug #X" comments, no `root_cause` fields, no remediation suggestions. The Bug Ticket Analyzer must parse actual stack traces and infer root causes like it would in a real production environment.

| Log File | Format | Key Features | Bug Type |
|----------|--------|--------------|----------|
| `error_001_drug_interaction_grafana_loki.log` | **Grafana Loki** (LogQL with K8s labels) | K8s metadata (namespace, pod, container), label-based filtering for modern K8s environments | DrugInteractionError - case-sensitive comparison issue |
| `error_002_invalid_dosage_splunk.log` | **Splunk** (key-value pairs) | Splunk sourcetype, index, host fields; key=value format for enterprise Splunk environments | ValueError (should be InvalidDosageError) - negative dosage value |
| `error_003_null_patient_elasticsearch.json` | **Elasticsearch/ELK** (flattened JSON) | @timestamp, dot-notation fields, K8s metadata for ELK Stack (Elasticsearch, Logstash, Kibana) | AttributeError - missing null check for patient object |
| `error_004_index_error_cloudwatch.json` | **AWS CloudWatch** (AWS native JSON) | CloudWatch log groups/streams, AWS ARNs, ECS task metadata for AWS environments | IndexError - accessing empty medication list |
| `error_005_validation_error_datadog.json` | **Datadog APM** (JSON with trace context) | ddtags, trace/span IDs, APM correlation, Datadog-specific fields for observability platform | ValidationError - invalid date format in Pydantic model |
| `error_006_key_error_prometheus.log` | **Prometheus** (Alertmanager format) | Metrics (counters, gauges), alert rules, correlated log entries for Prometheus/Grafana monitoring | KeyError - missing medication in DANGEROUS_INTERACTIONS dictionary |
| `error_007_type_error_syslog_batch.log` | **Syslog** (traditional batch format) | RFC 3164 syslog format, **repetitive errors (15+ occurrences)** to test noise filtering in batch jobs | TypeError - passing int instead of datetime object |

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
