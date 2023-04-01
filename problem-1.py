import random
array = [3,5,8,4,2]
n = random.choice(array)
prerange = array[:n]
postrange = array[n:]
sum(prerange)
if sum(prerange) == sum(postrange):
    print(f"yes n is {n} ")
elif sum(prerange) != sum(postrange):
    print(f"no n is {n} ")
else:
    print("error")
