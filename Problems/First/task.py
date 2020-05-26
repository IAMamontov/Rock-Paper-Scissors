# read test_file.txt
file_test = open("test_file.txt", "r", encoding="utf-16")
print(file_test.readlines()[0])
file_test.close()

