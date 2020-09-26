
class Calculator:
    result = 0
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

class FourCal:
    total_cal=0#클래스 전체 단위의 static 변수
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        FourCal.total_cal += 1
        return result
    def mul(self):
        result = self.first * self.second
        FourCal.total_cal += 1
        return result
    def sub(self):
        result = self.first - self.second
        FourCal.total_cal += 1
        return result
    def div(self):
        result = self.first / self.second
        FourCal.total_cal += 1
        return result

a = FourCal(4, 2)
print(a.first)
print(a.second)
print("ti : " + str(FourCal.total_cal))
a.add()
a.div()
print("ti : " + str(FourCal.total_cal))
print(a.total_cal)