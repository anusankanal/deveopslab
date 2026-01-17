def multiply(num, i):
    """
    Returns multiplication of num and i
    """
    return num * i


def multiplication_table(num):
    """
    Returns multiplication table (1 to 10) as a list
    """
    return [num * i for i in range(1, 11)]


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {multiply(num, i)}")
