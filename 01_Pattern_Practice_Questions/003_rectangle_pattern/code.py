def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.

    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.

    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    output = []
    row = "*" * m
    for _ in range(n):
        output.append(row)
    return output


if __name__ == "__main__":
    print(generate_rectangle(1, 1))
    print(generate_rectangle(3, 2))
    print(generate_rectangle(4, 5))

# Output
# ['*']
# ['**', '**', '**']
# ['*****', '*****', '*****', '*****']
