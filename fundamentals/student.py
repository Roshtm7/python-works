# write a program to read student name and 3 marks mark1,mark2,mark3 and print total mark and average mark

#program
stud_name=input("enter the student name:")
mark1=int(input("enter the mark1:"))
mark2=int(input("enter the mark2:"))
mark3=int(input("enter the mark3:"))
total_mark=mark1+mark2+mark3
avg_mark=(total_mark)/3
print(f"{total_mark } and {avg_mark}")