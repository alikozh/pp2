class String:
    def get_string(self):
        self.str = input()
       
    def print_string(self):
        print(self.str.upper())

p1 = String()

p1.get_string()
p1.print_string()


