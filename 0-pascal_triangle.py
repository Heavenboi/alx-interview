def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n: An integer representing the number of rows in the triangle.

    Returns:
    - A list of lists of integers representing Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  
        if i > 0:
            ''' Calculate other elements in the row using the previous row'''
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  
            ''' Last element in each row is always 1'''
        triangle.append(row)

    return triangle
