def solve(numheads, numlegs):
    x = numlegs - numheads * 2
    print("Rabbits:", x/2, "Chickens:", numheads - x/2)

solve(int(input("Heads:")), int(input("Legs:")))