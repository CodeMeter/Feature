name = input("Enter your name")
halfname = int(len(name)/2)
splitname = name[0:halfname]
otherhalf = name[halfname:int(len(name))]
print(splitname)
print(otherhalf)
