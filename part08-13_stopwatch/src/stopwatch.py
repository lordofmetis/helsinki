# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        return f"{self.minutes:0>2}:{self.seconds:0>2}"

    def tick(self):
        if self.seconds % 59 != 0:
            self.seconds += 1
        else:
            if self.seconds != 0:
                if self.minutes != 59:
                    self.minutes += 1
                else:
                    self.minutes = 0
                self.seconds = 0    
            else:
                self.seconds = 1

if __name__ == "__main__":          
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()