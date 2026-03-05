"""Main business logic for medication management."""

from __future__ import annotations

import datetime as dt

from medication_tracker.drug_interactions import check_drug_interaction
from medication_tracker.exceptions import InvalidDosageError
from medication_tracker.models import DoseRecord, Medication, Patient, Schedule


class MedicationService:
    """Service for managing patient medications."""

    def __init__(self) -> None:
        """Initialize the medication service."""
        self.schedules: dict[str, Schedule] = {}
        self.dose_history: dict[str, list[DoseRecord]] = {}

    def create_schedule(self, patient: Patient) -> Schedule:
        """
        Create a new medication schedule for a patient.

        Args:
            patient: Patient entity

        Returns:
            New schedule instance
        """
        schedule = Schedule(patient_id=patient.id)
        self.schedules[patient.id] = schedule
        return schedule

    def add_medication_to_schedule(
        self,
        patient_id: str,
        medication: Medication,
    ) -> None:
        """
        Add a medication to patient's schedule.

        Args:
            patient_id: Patient identifier
            medication: Medication to add

        Raises:
            InvalidDosageError: If dosage is invalid
            DrugInteractionError: If medication conflicts
        """
        schedule = self.schedules.get(patient_id)
        if schedule is None:
            raise ValueError(f"No schedule found for patient {patient_id}")

        # Validate dosage
        # Intentional bug: Doesn't handle negative dosages properly!
        if medication.dosage < 0:  # Line 78 - Bug #2
            # This should raise InvalidDosageError, but uses wrong exception
            raise ValueError(f"Invalid dosage: {medication.dosage}")

        # Check interactions
        check_drug_interaction(schedule.medications, medication)

        # Add to schedule
        schedule.add_medication(medication)

    def record_dose(
        self,
        patient_id: str,
        medication: Medication,
        administered_by: str,
    ) -> DoseRecord:
        """
        Record that a dose was administered.

        Args:
            patient_id: Patient identifier
            medication: Medication that was administered
            administered_by: Name of person who administered

        Returns:
            Dose record
        """
        record = DoseRecord(
            medication=medication,
            administered_at=dt.datetime.now(),
            administered_by=administered_by,
        )

        if patient_id not in self.dose_history:
            self.dose_history[patient_id] = []

        self.dose_history[patient_id].append(record)
        return record

    def get_next_dose_time(
        self,
        patient_id: str,
        medication_name: str,
    ) -> dt.datetime | None:
        """
        Calculate when the next dose is due.

        Args:
            patient_id: Patient identifier
            medication_name: Name of medication

        Returns:
            Timestamp of next dose, or None if never administered
        """
        history = self.dose_history.get(patient_id, [])

        # Filter for this specific medication
        med_history = [
            record for record in history if record.medication.name == medication_name
        ]

        if not med_history:
            return None

        # Intentional bug: Doesn't check if list is empty before accessing!
        last_dose = med_history[-1]  # Line 156 - Bug #4 (if med_history is empty)
        frequency = last_dose.medication.frequency_hours
        next_dose = last_dose.administered_at + dt.timedelta(hours=frequency)

        return next_dose
