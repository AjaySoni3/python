if 1>2:
    print('first block')
elif 3 ==3:
    print('true')
else:
    print("second block")

# for loop
seq = [1,2,3,4,5]

for item in seq:
    print('*')

d= {"sam":1,"frank": 2, "dan":3}

for item in d:
    print(item)

for k in d:
    print(k)
    print(d[k])

# tuple unpacking

my_pair = [(1,2),(3,4),(5,6)]

for tup1,tup2 in my_pair:
    print(tup1)
    print(tup2)

# while loop

i = 1

while i<5:
    print(f"i is. {i} ")
    i +=1

# range

print(list(range(0,21,2)))

for item in range(10):
    print(item)

# list comprehension

x = [1,2,3,4,5]

out = [num**2 for num in x ]
print(out)
