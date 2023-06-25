# Write your solution here
def longest(strings):
    result = "a"

    for i in strings:
        if len(i) > len(result):
            result = i
    return result



if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))