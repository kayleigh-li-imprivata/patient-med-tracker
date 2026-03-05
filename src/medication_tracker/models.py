"""Pydantic models for medication tracking."""

from __future__ import annotations

import datetime as dt
from typing import Any

from pydantic import BaseModel, Field, field_validator


class Patient(BaseModel):
    """Patient entity."""

    id: str = Field(description="Patient identifier", examples=["P-12345"])
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: str | None = Field(  # Bug #5: Should be dt.date, not str!
        default=None,
        description="Patient's date of birth",
        examples=["1990-01-15"],
    )

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_format(cls, v: str | None) -> str | None:
        """Validate date format."""
        if v is None:
            return v
        # Intentional bug: This will fail if date is in wrong format
        # Expected: YYYY-MM-DD, but doesn't handle other formats
        if len(v) != 10 or v[4] != "-" or v[7] != "-":
            raise ValueError(f"Invalid date format: {v}")  # Line 34 - Bug #5
        return v


class Medication(BaseModel):
    """Medication entity."""

    name: str = Field(description="Medication name", examples=["Aspirin", "Warfarin"])
    dosage: float = Field(
        description="Dosage amount in mg",
        examples=[100.0, 250.5],
    )
    frequency_hours: int = Field(
        description="Hours between doses",
        examples=[6, 8, 12, 24],
    )

    @field_validator("dosage")
    @classmethod
    def validate_positive_dosage(cls, v: float) -> float:
        """Ensure dosage is positive."""
        if v <= 0:
            raise ValueError("Dosage must be positive")
        return v


class DoseRecord(BaseModel):
    """Record of a medication dose administration."""

    medication: Medication
    administered_at: dt.datetime
    administered_by: str | None = None


class Schedule(BaseModel):
    """Medication schedule for a patient."""

    patient_id: str
    medications: list[Medication] = Field(default_factory=list)
    start_date: dt.datetime = Field(default_factory=dt.datetime.now)

    def add_medication(self, medication: Medication) -> None:
        """Add a medication to the schedule."""
        self.medications.append(medication)
