class Mynums:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        
        x = self.start
        self.start+=1
        return x

nums = Mynums(1, 20)    

for i in nums:
    print(i, end = ' ')

