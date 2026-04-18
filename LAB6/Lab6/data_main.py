from data_package import strip_whitespace, remove_duplicates, calculate_mean, find_maximum


def main():
    raw_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8, 21): ")


    string_list = raw_input.split(',')


    cleaned_strings = strip_whitespace(string_list)


    try:

        num_list = [float(num) for num in cleaned_strings if num]
    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")
        return


    unique_data = remove_duplicates(num_list)


    print(f"Cleaned and unique data: {unique_data}")
    print(f"Mean: {calculate_mean(unique_data):.2f}")
    print(f"Maximum: {find_maximum(unique_data)}")


if __name__ == "__main__":
    main()