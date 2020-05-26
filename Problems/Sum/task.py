# read sums.txt
file_sums = open("sums.txt", "r")
for s in file_sums:
    a, b = map(int, s.split())
    print(a + b)
file_sums.close()