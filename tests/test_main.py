from app.main import create_assignment


def test_create_assignment():
    assignment = create_assignment(
        "Practical 5",
        "Computer Networks",
        "Submit the practical"
    )

    assert assignment.title == "Practical 5"
    assert assignment.subject == "Computer Networks"
    assert assignment.description == "Submit the practical"