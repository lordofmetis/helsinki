def longest_series_of_neighbours(numbers):
    longest_series = 0
    current_series = 0

    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) == 1:
            current_series += 1
            longest_series = max(longest_series, current_series)
        else:
            current_series = 0

    return longest_series + 1 if longest_series > 0 else 0


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
