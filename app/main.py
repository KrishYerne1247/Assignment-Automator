from app.models import Assignment
from app.validator import validate_assignment


def create_assignment(
    title: str,
    subject: str,
    description: str
) -> Assignment:
    assignment = Assignment(
        title=title,
        subject=subject,
        description=description
    )

    validate_assignment(assignment)

    return assignment


def main() -> None:
    try:
        assignment = create_assignment(
            "Practical 5 Submission",
            "Computer Networks",
            "Submit the practical file."
        )

    except TypeError as error:
        print("Type error:", error)

    except ValueError as error:
        print("Validation error:", error)

    else:
        print("Assignment is valid:")
        print(assignment)

    finally:
        print("Assignment processing finished.")


if __name__ == "__main__":
    main()