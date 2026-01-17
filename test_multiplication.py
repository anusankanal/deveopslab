from multiplication import multiply, multiplication_table


def test_multiply_positive_numbers():
    assert multiply(5, 2) == 10


def test_multiply_with_zero():
    assert multiply(7, 0) == 0


def test_multiplication_table_of_3():
    assert multiplication_table(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
