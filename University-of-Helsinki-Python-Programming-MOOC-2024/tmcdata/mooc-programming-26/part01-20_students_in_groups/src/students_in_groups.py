# Write your solution here

student_no = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))

if (student_no / group_size) % 2 == 0:
    print(f"Number of groups formed: {int(student_no / group_size)}")
else:
    print(f"Number of groups formed: {(student_no // group_size)+1}")
