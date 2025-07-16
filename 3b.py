first_name = "Chandan"
last_name = "Gowda"
full_name = first_name + " " + last_name
print(full_name)

# repetition
message = "This is a Warning! "
print(message*10)

'''
message = "This is a Warning!"
for _ in range(10):
    print(message)
Output:
pgsql
Copy
Edit
This is a Warning!
This is a Warning!
This is a Warning!
This is a Warning!
This is a Warning!
This is a Warning!
This is a Warning!
This is a Warning!
This is a Warning!
This is a Warning!
'''

print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("Warning", "Error"))

name = '''chandan said "hello"
        darshan said "hi"
        '''
print(len(message)) # length

name = "chandan"
print(name[4]) # index = position - 1
print(name[2:6])
print(name[2:])
print(name[:4])
print(name[-2])
print(name[::3])

s = "chandan \tis a good boy"
print(s)
