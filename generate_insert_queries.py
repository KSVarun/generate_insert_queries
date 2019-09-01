# object reading from file
f = open("data.csv", "r")
# object to write to a file
fw = open("data.sql", "w+")
contents = f.readlines()

# get number of lines of input, to figure of number of insert statements required
numOfLines = len(contents)

name = []

# seperate based on comma(,)
for i in range(0, numOfLines):
    name.append(contents[i].split(","))

# remove the ending new line character
for i in range(0, numOfLines):
    name[i][-1] = name[i][-1].rstrip()

# finding the number of elements or columns
numOfElements = len(name[0])

l = 1
for i in range(0, numOfLines-1):

    one = "insert into topics("
    for j in range(numOfElements):
        one = one+name[0][j]+","
    one = one[:-1]
    one = one+") values("

    for k in range(numOfElements):
        one = one+name[l][k]+","
    one = one[:-1]
    one = one+");\n"
    if(l != numOfLines-1):
        l = l+1
    fw.write(one)

fw.close()
f.close()
