import math

def main():
    while True:
        print(" Choose task: "
              "\n1. Task 1\n2.Task2\n3.Task3\n4.Close")
        ch = int(input("Enter task "))

        if ch == 1: print (task1())
        elif ch == 2: print (task2())
        elif ch == 3: print(task3())
        elif ch == 4: exit()

def task1():
    number = int(input("Enter number "))
    tens = int(number % 100 / 10)
    nums = int(number % 100 % 10)
    hundreds = int(number / 100)

    return ((hundreds * 100) + (nums * 10) + tens)
def task2():
    x = float(input())
    primer1 = math.sin(3 * x + math.radians(15))
    primer1cube = pow(primer1, 3)

    primer2 = math.fabs(2 * x)

    log_argument = primer1cube*primer2

    if(log_argument) <= 0:
        return "log argument is negative"

    up = math.log((log_argument), 3)
    down = pow(3, (2*x-1))*math.cbrt(4*3.14+1/2*math.cos(x))
    result = up / down

    return result

def task3():
    x = int(input())
    y = int(input())

    if x < 0 and y > 0: return "Точка належить другій координатній чверті"
    else: return "Точка не належить другій координатній чверті"

main()
