# Copy here code of line function from previous exercise
def line(times, text):
    if text != "":
        print(text[0] * times)
    else:
        print("*" * times)

def square(size, character):
    # You should call function line here with proper parameters
    n = 1
    while n <= size:
        line(size, character[0])
        n += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")