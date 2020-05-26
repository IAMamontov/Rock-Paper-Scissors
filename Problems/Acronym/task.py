# read test.txt
file_test = open("test.txt", "r")
for i in file_test.readlines():
    print(i[0])
file_test.close()