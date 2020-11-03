"""In-line lambda functions"""


addition = lambda x, y:  x+y


print(addition(x=1, y=2))

print(addition(x='hello', y='world'))

"""Other cool in-line operations"""

names = ["Name A", "Name B", "Name D", "Name C"]
# .lower() doesn't work on >3.8 :(
print(sorted(names, key=lambda name: name.split()[-1].lower()))

# if you do not set n=n initially it thinks that n == 0 on every iter
funcs = [lambda x, n=n: x+n for n in range(6)]
for f in funcs:
    print(f(0))
