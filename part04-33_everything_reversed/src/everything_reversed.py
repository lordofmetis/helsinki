# Write your solution here
def everything_reversed(my_list):
    bee_list = []
    for item in my_list:
        bee_list.append(item[::-1])
    
    i = len(bee_list) - 1
    new_list = []
    while i >= 0:
        new_list.append(bee_list[i])
        i -= 1
    
    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)