# Write your solution here
def list_sum(a, b):
    new_list = []
    for i in range(len(a)):
        sum_item = a[i] + b[i]
        new_list.append(sum_item) 
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
