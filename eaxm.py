s = 'django'
print(s[0])
print(s[-1])
print(s[0:-2])
print(s[1:-2])
print(s[-2:])
print(s[::-1])

l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l)

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
x = set(mylist)
print(x)

age = 4
name = "Sammy"
print(("hello my dog's name is {} and he is {} year old " .format(name,age)))
