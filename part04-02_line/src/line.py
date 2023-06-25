# Write your solution here
def line(times, text):
    if text != "":
        print(text[0] * times)
    else:
        print("*" * times)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")