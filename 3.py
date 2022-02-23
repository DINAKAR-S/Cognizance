# Write a python program to make a 2-dimensional list that contains represents a table of records, for instance, student details like Roll no, Student Name, Marks;
lst = []
n = int(input("Enter number of rows : "))
print("Enter the roll number , name and marks respectively to output a data table")
for i in range(0, n):
    ele = [input(), input(),input()]
    lst.append(ele)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for a in lst:
    for b in a:
        print(b,end=" "*10)
    print()
 