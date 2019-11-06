import pytest

import reusable_program


@pytest.mark.parametrize("name,age,want", [
    pytest.param(
        "Rodolfo", "42",
        "Rodolfo will be 100 years old in the year 2072",
        id="Rodolfo",
    ),
    pytest.param(
        "Marion", "24",
        "Marion will be 100 years old in the year 2090",
        id="Marion",
    ),
])
def test_reusable_program(name, age, want):
    got = reusable_program.greet_100(name, age)
    assert got == want

@pytest.mark.parametrize("name,age,want", [
    pytest.param(
        "hop", "I don't know the answer",
        ValueError("Sorry, I could not understand your age!"),
        id="hop",
    ),
])
def test_reusable_program_bad_input(name, age, want):
    with pytest.raises(want.__class__) as exception:
        reusable_program.greet_100(name, age)
        assert exception == want
