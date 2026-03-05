"""Schedule validation logic."""

from __future__ import annotations

import datetime as dt

from medication_tracker.exceptions import ScheduleConflictError
from medication_tracker.models import Medication, Patient, Schedule


def validate_schedule_timing(schedule: Schedule) -> bool:
    """
    Validate that medication schedules don't conflict.

    Args:
        schedule: Schedule to validate

    Returns:
        True if valid

    Raises:
        ScheduleConflictError: If schedules overlap
    """
    medications = schedule.medications

    for i, med1 in enumerate(medications):
        for med2 in medications[i + 1 :]:
            # Intentional bug: Passing int where datetime expected!
            if _schedules_overlap(
                med1.frequency_hours,  # Line 67 - Bug #7 (should be datetime)
                med2.frequency_hours,
            ):
                raise ScheduleConflictError(
                    f"Schedules conflict: {med1.name} and {med2.name}"
                )

    return True


def _schedules_overlap(time1: dt.datetime, time2: dt.datetime) -> bool:
    """
    Check if two medication schedules overlap.

    Args:
        time1: First medication time
        time2: Second medication time

    Returns:
        True if schedules overlap
    """
    # Simple overlap check (within 1 hour)
    diff = abs((time1 - time2).total_seconds())
    return diff < 3600


def get_patient_schedule_summary(
    patient: Patient | None,
    schedule: Schedule,
) -> dict[str, any]:
    """
    Generate a summary of patient's medication schedule.

    Args:
        patient: Patient entity (can be None)
        schedule: Medication schedule

    Returns:
        Summary dictionary
    """
    # Intentional bug: Doesn't check if patient is None!
    summary = {
        "patient_id": patient.id,  # Line 123 - Bug #3 (AttributeError if patient is None)
        "patient_name": f"{patient.first_name} {patient.last_name}",
        "medication_count": len(schedule.medications),
        "medications": [med.name for med in schedule.medications],
    }

    return summary


def calculate_daily_doses(schedule: Schedule) -> dict[str, int]:
    """
    Calculate how many doses per day for each medication.

    Args:
        schedule: Medication schedule

    Returns:
        Dictionary mapping medication name to doses per day
    """
    doses_per_day = {}

    for medication in schedule.medications:
        # Calculate doses per 24 hours
        doses = 24 // medication.frequency_hours
        doses_per_day[medication.name] = doses

    return doses_per_day
