import pytest


# Guess the output of the program
@pytest.mark.run(order=-3)
def test_b():
    print('Test_B method execution...')


@pytest.mark.run(order=-1)
def test_c():
    print('Test_C method execution...')


@pytest.mark.run(order=-2)
def test_a():
    print('Test_A method execution...')
