f = open('Countries.txt')
file_data = f.read()
f.close()
print(file_data)

# Create a new file and write content in it
f = open('dummyfile.txt', 'w')
f.write("Hello there!")
f.close()

# No need to close file explicitly by using with keyword
with open('Countries.txt', 'r') as f:
    file_data = f.read()
    print(file_data)


# Reading part of the file by passing an int argument to read function
with open('Countries.txt', 'r') as country:
    print(country.read(5))
    print(country.read(52))
    print(country.read())


# Strip of newline character to show output in a single line
camelot_lines = []
with open("Countries.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)


def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    # use the for loop syntax to process each line
    # and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            cast_list.append(line.split(',')[0])
    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
