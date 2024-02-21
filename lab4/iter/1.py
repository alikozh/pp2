class Mynums:
    def __iter__(self):
        self.a = -30
        return self
    
    def __next__(self):
        x = self.a
        self.a += 2
        return x
    
nums = Mynums()

myiter = iter(nums)

for i in range(10):
    print(next(myiter))