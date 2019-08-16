s = 'Aashirbad maharana  '
print(s )
print(s[:10 : ])


print( len(s)) # len

# slicing
print(s[: 11])
print(s[-2])
print(s [-5 : -1])


print(s)
print(s.strip()) # eliminate space
print(s.lstrip())# eliminate spaces at left side
print(s.rstrip())

print(s)
# find() to locate the substring
print(s.find("rbad",0,13 ))
print(s.count("A"))

print(s.replace("s","S"))
print(s.upper())
