class Calculator:
    
    def __init__(self, input1, input2):
        self.input1 = float(input1)
        self.input2 = float(input2)

    def adder(self):
        return self.input1 + self.input2

    def subtractor(self):
        return self.input1 - self.input2

    def multiplier(self):
        return self.input1 * self.input2
    
    def divider(self):
        if(self.input2 == 0):
            return 0
        else:
            return self.input1 / self.input2

    def clear(self):
        self.input1 = 0
        self.input2 = 0


input1  = input("Enter 1st number: ")
input2  = input("Enter 2nd number: ")
c = Calculator(input1, input2)
sum = c.adder()
print(sum)

sub = c.subtractor()
print(sub)
c.clear()
mul = c.multiplier()
print(mul)

div = c.divider()
print(div)



print(c.adder())
