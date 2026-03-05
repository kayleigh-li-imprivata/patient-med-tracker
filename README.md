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

### 1. Grafana Loki Format (`error_001_drug_interaction_grafana_loki.log`)
- **Format:** LogQL with Kubernetes labels
- **Features:** K8s metadata (namespace, pod, container), label-based filtering
- **Use Case:** Modern Kubernetes environments with Grafana/Loki stack
- **Bug:** DrugInteractionError - case-sensitive comparison issue

### 2. Splunk Format (`error_002_invalid_dosage_splunk.log`)
- **Format:** Key-value pairs with Splunk metadata
- **Features:** Splunk sourcetype, index, host, key=value format
- **Use Case:** Enterprise environments using Splunk Enterprise
- **Bug:** ValueError (should be InvalidDosageError) - negative dosage value

### 3. Elasticsearch/ELK Format (`error_003_null_patient_elasticsearch.json`)
- **Format:** Flattened JSON with dot-notation fields
- **Features:** @timestamp, @version, K8s metadata, flattened structure
- **Use Case:** ELK Stack (Elasticsearch, Logstash, Kibana)
- **Bug:** AttributeError - missing null check for patient object

### 4. AWS CloudWatch Format (`error_004_index_error_cloudwatch.json`)
- **Format:** AWS native JSON with ECS metadata
- **Features:** CloudWatch log groups/streams, AWS ARNs, ECS task metadata
- **Use Case:** AWS environments with CloudWatch Logs
- **Bug:** IndexError - accessing empty medication list

### 5. Datadog Format (`error_005_validation_error_datadog.json`)
- **Format:** Datadog APM JSON with trace context
- **Features:** ddtags, trace/span IDs, APM correlation, Datadog-specific fields
- **Use Case:** Datadog APM and logging platform
- **Bug:** ValidationError - invalid date format in Pydantic model

### 6. Prometheus Format (`error_006_key_error_prometheus.log`)
- **Format:** Prometheus metrics export with alert context
- **Features:** Metrics (counters, gauges, histograms), alert rules, PromQL queries
- **Use Case:** Prometheus/Grafana monitoring with Alertmanager
- **Bug:** KeyError - missing medication in DANGEROUS_INTERACTIONS dictionary
- **Special:** Includes metrics, alert details, and correlated log entry

### 7. Syslog Format (`error_007_type_error_syslog_batch.log`)
- **Format:** Traditional syslog with batch processing
- **Features:** RFC 3164 syslog format, repetitive errors (15+ occurrences)
- **Use Case:** Traditional Unix/Linux systems, batch job monitoring
- **Bug:** TypeError - passing int instead of datetime object
- **Special:** Simulates batch job with high-volume repetitive errors (tests noise filtering)

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
