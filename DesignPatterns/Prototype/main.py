from zombie import *

z = Zombie(100, sword = Sword(100))

arr = []
for i in range(100):
    arr.append(Zombie(100, sword = Sword(100)))

arr[0].health = 0
arr[0].sword.val = 9
print(arr[0].sword.val)
print(arr[1].sword.val)