class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

print("Countdown from 5:")
for num in Countdown(5):
    print(num)

print("\nManual countdown from 3:")
counter = Countdown(3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))