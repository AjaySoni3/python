my_stuff = {"key1":123,"key2" : "value2", "key3" :{'123': [1,2,'grabme']}}
print(my_stuff['key3']['123'][2].upper())
my_stuff['key1'] = "456"
print(my_stuff)
