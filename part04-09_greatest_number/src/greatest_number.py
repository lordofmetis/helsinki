# Write your solution here
def greatest_number(a, b, c):
    if a >= b > c:
        return a
    elif a >= c > b:
        return a
    elif b >= a > c:
        return b
    elif b >= c > a:
        return b
    elif c >= a > b:
        return c    
    else:
        return c



  

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)