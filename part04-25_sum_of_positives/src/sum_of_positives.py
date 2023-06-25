# Write your solution here

def sum_of_positives(my_list):
    new_list = []
    for i in my_list:
        if i > 0:
            new_list.append(i)
    return sum(new_list)
        


        
    





if __name__ == "__main__":
    my_list = [1, -1, 2, -2, 3, -3]
    result = sum_of_positives(my_list)
    print("The result is", result)
