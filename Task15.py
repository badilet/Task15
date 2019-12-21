# Write the code, which will print numbers from 0 till your age. And if your age
# is odd, will be printed all odd numbers till your age, if even all even numbers.

age = int(input("Enter your age:"))
for i in range(0, age, +1):
    print(i)

if age % 2 == 0:
    for i in range(0, age, +2):
        print(i)
else:
    for i in range(1, age, +2):
        print(i)
