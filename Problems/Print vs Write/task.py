numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file_list = open("file_with_list.txt", "w")
print(numbers, file=file_list, end="")
file_list.close()