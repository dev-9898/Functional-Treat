data = []

print("Welcome to the Data Analyzer and Transformer Program")

def print_summary(**kwargs):
    """Print Summary Using **kwargs"""
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

while True:
    print("\nMain Menu")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Enter Your Choice: "))

    match choice:
        case 1:
            data = list(map(int, input(
                "Enter data for a 1D array (comma separated): "
            ).split(",")))
            print("Data has been Stored Successfully")
            print(*data)

        case 2:
            if not data:
                print("Data Not Found")
            else:
                total = len(data)
                minimum = min(data)
                maximum = max(data)
                total_sum = sum(data)
                average = round(total_sum / total, 2)

                print("\nData Summary")
                print_summary(
                    **{
                        "Total Elements": total,
                        "Minimum Value": minimum,
                        "Maximum Value": maximum,
                        "Sum of all values": total_sum,
                        "Average value": average
                    }
                )

        case 3:
            sub = int(input("Enter a number to calculate its factorial: "))

            def factorial(n):
                if n == 0 or n == 1:
                    return 1
                return n * factorial(n - 1)

            result = factorial(sub)
            print(f"Factorial of {sub} is:", result)

        case 4:
            if not data:
                print("Data Not Found")
            else:
                threshold = int(input(
                    "Enter a threshold value to filter out data above this value: "
                ))

                filtered_data = list(filter(lambda x: x >= threshold, data))

                print(f"Filtered Data (Values >= {threshold}):")
                print(*filtered_data, sep=", ")

        case 5:
            if not data:
                print("Data Not Found")
            else:
                print("Choose sorting option:")
                print("1. Ascending")
                print("2. Descending")

                sort_choice = int(input("Enter your choice: "))

                if sort_choice == 1:
                    sorted_data = sorted(data)
                    print("Sorted Data in Ascending Order:")
                    print(*sorted_data, sep=", ")

                elif sort_choice == 2:
                    sorted_data = sorted(data, reverse=True)
                    print("Sorted Data in Descending Order:")
                    print(*sorted_data, sep=", ")

                else:
                    print("Invalid sorting choice")

        case 6:
            if not data:
                print("Data Not Found")
            else:
                def dataset_statistics(data):
                    minimum = min(data)
                    maximum = max(data)
                    total = sum(data)
                    average = total / len(data)
                    return minimum, maximum, total, round(average, 2)

                min_val, max_val, total_val, avg_val = dataset_statistics(data)

                print("\nDataset Statistics:")
                print("- Minimum value:", min_val)
                print("- Maximum value:", max_val)
                print("- Sum of all values:", total_val)
                print("- Average value:", avg_val)

        case 7:
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        case _:
            print("Invalid Choice...")
