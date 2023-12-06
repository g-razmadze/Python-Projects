def pro_prod_tbl(num_rows, num_columns):
    """
    This function takes two integers as input and prints a product table of the specified size.

    Args:
        num_rows (int): The number of rows in the table.
        num_columns (int): The number of columns in the table.

    Returns:
        None
    """
    for i in range(1, num_rows + 1):
        print(i, end=' |\t ')
        for n in range(1, num_columns + 1):
            print(i * n, end=' \t ')
        print()

def main():
    """Main Function"""
    pro_prod_tbl(5, 5)


if __name__ == "__main__":
    main()
