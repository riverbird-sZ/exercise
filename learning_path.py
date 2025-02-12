from pathlib import Path

path = Path("exercise")
print(path.exists())

path1 = Path("PycharmProjects")
print(path1.exists())

path2 = Path("nested_loop.py")
print(path2.exists())

#path_cr = Path("Testing")
#print(path.mkdir())


# path_ct = Path("Hello again")
# print(path.mkdir())

path = Path()
for file in path.glob("*.py"):
    print(file)

















