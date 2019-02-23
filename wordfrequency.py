s = input("Enter a string: ")
l = list(s.split())
d = {}
for i in l:
    d[i]=l.count(i)
print(d)
