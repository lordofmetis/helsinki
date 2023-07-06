# Write your solution here:
class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    def __str__(self):
        return f"{self.hours:0>2}:{self.minutes:0>2}:{self.seconds:0>2}"

    def set(self, hour: int, minute: int, second: int = 0):
        self.hours = hour
        self.minutes = minute
        self.seconds = second
            
    def tick(self):
        if self.seconds != 59:
            self.seconds += 1
        else:
            if self.seconds != 0:
                if self.minutes != 59:
                    self.minutes += 1
                else:
                    if self.hours != 23:
                        self.hours += 1
                        self.minutes = 0
                    else:
                        self.hours = 0
                        self.minutes = 0
                        self.seconds = 0
                self.seconds = 0    
            else:
                self.seconds = 1

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)