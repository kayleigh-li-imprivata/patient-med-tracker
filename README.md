# Patient Medication Tracker

Fake hospital medication tracking application for testing the Bug Ticket Analyzer agent.

## Purpose

This is a **synthetic codebase** with intentional bugs designed to test automated bug analysis tools.

## Structure

- `src/medication_tracker/` - Main application code
- `logs/` - Error logs with stack traces (generated separately)

## Intentional Bugs

This codebase contains 7 intentional bugs:
1. Drug interaction error (case-sensitive comparison)
2. Invalid dosage error (negative value)
3. Null pointer error (missing patient check)
4. Index error (empty list access)
5. Validation error (invalid date format)
6. Key error (missing medication lookup)
7. Type error (wrong argument type)

## DO NOT USE IN PRODUCTION

This code is intentionally buggy and should never be used in a real healthcare setting.
