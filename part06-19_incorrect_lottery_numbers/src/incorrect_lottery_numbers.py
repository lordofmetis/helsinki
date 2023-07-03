def filter_incorrect():

    with open("lottery_numbers.csv") as new_file:
        with open("correct_numbers.csv", "w") as newer_file:
            for line in new_file:
                line = line.strip()
                parts = line.split(";")

                # Check if the line has two parts: week and numbers
                if len(parts) != 2:
                    continue

                week, numbers = parts

                # Check if the week part is in the correct format
                if not week.startswith("week ") or not week[5:].isdigit():
                    continue

                int_numbers = numbers.split(",")

                # Check if there are exactly 7 numbers
                if len(int_numbers) != 7:
                    continue

                # Check if all numbers are valid integers between 1 and 39 (inclusive)
                valid_numbers = True
                unique_numbers = set()
                for int_number in int_numbers:
                    if not int_number.isdigit() or not (1 <= int(int_number) <= 39):
                        valid_numbers = False
                        break
                    if int_number in unique_numbers:  # Check for duplicate numbers
                        valid_numbers = False
                        break
                    unique_numbers.add(int_number)

                if not valid_numbers:
                    continue

                # If all checks pass, write the line to the output file
                newer_file.write(f"{week};{numbers}\n")


if __name__ == "__main__":
    filter_incorrect()