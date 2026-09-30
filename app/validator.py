from app.models import Assignment


def validate_assignment(assignment: Assignment) -> None:
    if not isinstance(assignment.title, str):
        raise TypeError("Assignment title must be a string.")

    if not isinstance(assignment.subject, str):
        raise TypeError("Assignment subject must be a string.")

    if not isinstance(assignment.description, str):
        raise TypeError("Assignment description must be a string.")

    if not assignment.title.strip():
        raise ValueError("Assignment title cannot be empty.")

    if not assignment.subject.strip():
        raise ValueError("Assignment subject cannot be empty.")