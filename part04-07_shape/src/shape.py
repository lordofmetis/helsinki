def line(times, text):
    if text != "":
        print(text[0] * times)
    else:
        print("*" * times)

def triangle(times, text):
    i = 1
    while i <= times:
        line(i, text)
        i += 1

def square(times, height, character):
    j = 1
    while j <= height:
        line(times, character)
        j += 1

def shape(times, text, height, character):
    triangle(times, text)
    square(times, height, character)

if __name__ == "__main__":
    shape(5, "x", 2, "o")