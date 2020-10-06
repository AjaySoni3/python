def my_func(param1 = "default"):
    print(f"my first python function! {param1}")

my_func()

def hello():
    print('hello')

hello()

# return
def hello():
    return 'hello'

result = hello()
print(result)

# adding two number function
def addNum(num1,num2):
    if type(num1)==type(num2)== type(10):
        return num1 + num2
    else :
        return "Sorry i need integers!"

result = addNum('2',3)
print(result)

# lambda expression

my_lists = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2==0

even = filter(even_bool,my_lists)
print(list(even))


even = filter(lambda num:num%2==0,my_lists)
print(list(even))
