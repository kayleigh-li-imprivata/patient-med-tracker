"""Custom exceptions for medication tracking."""

from __future__ import annotations


class MedicationError(Exception):
    """Base exception for medication-related errors."""

    pass


class DrugInteractionError(MedicationError):
    """Raised when medications have dangerous interactions."""

    pass


class InvalidDosageError(MedicationError):
    """Raised when dosage is invalid or out of range."""

    pass


class ScheduleConflictError(MedicationError):
    """Raised when medication schedules conflict."""

    pass
