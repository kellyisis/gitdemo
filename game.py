import random

x = random.randint(1, 50)
print(x)
y = int(input("請猜一個數字"))
if x == y:
    print("猜對了!")
else:
    print("猜錯了~~")
