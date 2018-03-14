# file open and write, close
f = open("test.txt","w") # file path with mod like read, write, read binary, write binary...
f.write("123456")
f.close()

# write with print
f = open("test.txt", "w")
print("TEST", file=f)
f.close()

# open file with "with" syntax, i like this case
with open("test.txt","w") as f:
    print("GOOD with syntax", file=f)

# read file
with open("test.txt", "r") as f:
    print(f.readline())