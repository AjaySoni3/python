# checking sequence
def arrayCheck(nums):
     for i in range(len(nums)-2):
         if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] ==3:
             return True
     return False


result = arrayCheck([1,2,1,1,2,3])
print(result)

#return a new string made of every other character

def stringBits(str):
    x = str[::2]
    return x

result = stringBits('Heeololeo')
print(result)

#return True if either of the strings appears at the very end
# of the other string

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    return a[-len(b):] == b or a == b[-len(a):]

result = end_other('Hiabc', 'abc')
print(result)



def doubleChar(str):
    result = ''
    for char in str:
        result += char*2
    return result

y = doubleChar('The')
print(y)


def no_teen_sum(a, b, c):

        return fix_teen(a)+fix_teen(b)+fix_teen(c)


def fix_teen(n):
  if n in [13,14,17,18,19,]:
      return 0
  return n


y =no_teen_sum(11, 5, 13)
print(y)


def count_evens(nums):
    count = 0

    for element in nums:
        if element%2==0:
            count +=1
    return count

y = count_evens([2, 1, 2, 3, 4])
print(y)
