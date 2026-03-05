"""Drug interaction checking logic."""

from __future__ import annotations

from medication_tracker.exceptions import DrugInteractionError
from medication_tracker.models import Medication

# Known dangerous drug interactions
DANGEROUS_INTERACTIONS: dict[str, list[str]] = {
    "Warfarin": ["Aspirin", "Ibuprofen", "Naproxen"],
    "Aspirin": ["Warfarin"],
    "Metformin": ["Alcohol"],
    "Lisinopril": ["Potassium"],
}


def check_drug_interaction(
    existing_medications: list[Medication],
    new_medication: Medication,
) -> None:
    """
    Check if new medication conflicts with existing ones.

    Args:
        existing_medications: List of medications patient is already taking
        new_medication: New medication to check

    Raises:
        DrugInteractionError: If dangerous interaction detected
    """
    for existing in existing_medications:
        # Intentional bug: Case-sensitive comparison!
        # "warfarin" != "Warfarin", so interaction won't be detected
        if existing.name in DANGEROUS_INTERACTIONS:  # Line 45 - Bug #1
            conflicts = DANGEROUS_INTERACTIONS[existing.name]
            if new_medication.name in conflicts:
                raise DrugInteractionError(
                    f"{new_medication.name} conflicts with {existing.name}"
                )


def get_interaction_details(medication_name: str) -> list[str]:
    """
    Get list of medications that interact with the given medication.

    Args:
        medication_name: Name of the medication

    Returns:
        List of conflicting medication names

    Raises:
        KeyError: If medication not found in database
    """
    # Intentional bug: No error handling for missing key!
    # Will raise KeyError if medication not in dict
    interactions = DANGEROUS_INTERACTIONS[medication_name]  # Line 89 - Bug #6
    return interactions


def validate_medication_list(medications: list[Medication]) -> bool:
    """
    Validate that no medications in the list conflict with each other.

    Args:
        medications: List of medications to validate

    Returns:
        True if no conflicts found

    Raises:
        DrugInteractionError: If any conflicts detected
    """
    for i, med1 in enumerate(medications):
        for med2 in medications[i + 1 :]:
            check_drug_interaction([med1], med2)
    return True
