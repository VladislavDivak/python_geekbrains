class ComplexNumber:
    def __init__(self, real_part, imag_part):
        self.rp = real_part
        self.ip = imag_part

    def __str__(self):
        if self.ip == 0:
            return f'{self.rp:.2f}'
        if self.ip < 0:
            return f'{self.rp:.2f} - {abs(self.ip):.2f}i'
        else:
            return f'{self.rp:.2f} + {self.ip:.2f}i'

    def __add__(self,object):
        new_comp_num = ComplexNumber(self.rp + object.rp, self.ip + object.ip)
        return new_comp_num

    def __sub__(self,object):
        new_comp_num = ComplexNumber(self.rp - object.rp, self.ip - object.ip)
        return new_comp_num

    def __mul__(self,object):
        new_comp_num = ComplexNumber(self.rp*object.rp - self.ip*object.ip, self.rp*object.ip + self.ip*object.rp)
        return new_comp_num

    def __truediv__(self,object):
        new_rp = (self.rp*object.rp + self.ip*object.ip)/(object.rp**2 + object.ip**2)
        new_ip = (self.ip*object.rp - self.rp*object.ip)/(object.rp**2 + object.ip**2)
        new_comp_num = ComplexNumber(new_rp, new_ip)
        return new_comp_num

num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(2, 3)

print(num1)
print(num2)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)