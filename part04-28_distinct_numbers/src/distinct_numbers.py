# Write your solution here
def distinct_numbers(my_list):
    my_list = set(my_list)
    my_list = list(my_list)
    my_list = sorted(my_list)
    return my_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 10000]
    print(distinct_numbers(my_list)) # [1, 2, 3]