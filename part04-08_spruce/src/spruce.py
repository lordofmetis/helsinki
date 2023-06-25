# Write your solution here

def spruce(n):
    print("a spruce!")
    i = 1
    while i <= n:
        print((n - i) * " " + "*" * (2 * i - 1))
        i += 1
    print((n - 1) * " " + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce()