try:
    f = open("simple.txt","w")
    f.write("test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND OR READ DATA!")
finally:
    print("i always work on matter what!")
