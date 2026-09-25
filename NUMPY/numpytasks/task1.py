import numpy as np
marks = np.array([78, 65, 89, 45, 92, 56, 73, 88, 61, 95])
ages = np.array([20, 21, 19, 22, 20, 23, 21, 19, 22, 20])
sales = np.array([12000, 15000, 8000, 22000, 18000, 9500, 14000, 25000, 11000, 20000])


# Part A – Array Creation & Basics
# 1. Create a NumPy array containing the numbers from 10 to 30.
arr1=np.arange(10,31)
print(arr1)

# 2. Create an array containing 10 zeros.
arr2=np.zeros(10,int)
print(arr2)

# 3. Create an array containing 8 ones.
arr3=np.ones(8,int)
print(arr3)

# 4. Create an array containing even numbers from 2 to 20 using NumPy.
arr4=np.arange(2,21)
even=arr4[np.where(arr4 % 2==0)]
print(even)


# 5. Display the following for the marks array:
#  number of elements,
print(marks.size)
#  dimensions, shape,
print(marks.ndim)
#  and data type
print(marks.dtype)

# =================================================================

# Part B – Indexing & Slicing

# 6. From the marks array,
#  print the first element,
print(marks[0])
#  last element,
print(marks[-1])
#  third element,
print(marks[2])
#  and fifth element.
print(marks[4])


# 7. Print the first 5 elements of marks.
print(marks[0:5])

# 8. Print the last 4 elements of marks.
print(marks[-4:])
# 9. Print every alternate element from marks.
print(marks[0::2])
# 10. Print the elements of marks in reverse order.
print(marks[::-1])

# =================================================================

# Part C – NumPy Mathematical Operations

# 11. Add 5 marks to every student's marks. Do this using NumPy without using a loop.
# marks=marks+5
# print(marks)
print(marks.__add__(5))


# 12. Increase every value in sales by 10%.
ten=sales+sales/10
print(ten)


# 13. Find the total sales.
print(np.sum(sales))

# 14. Find the average marks.
print(np.average(marks))


# 15. Find the maximum mark, 
# minimum mark, 
# and difference between maximum and minimum mark.
print("maximum marks = ",np.max(marks))
print("minimum marks = ",np.min(marks))
print("difference = ",np.max(marks)-np.min(marks))
# =================================================================

# Part D – Conditions & Boolean Indexing

# 16. Find all students who scored more than 75 marks.
print(marks[np.where(marks>75)])

# 17. Find all students who scored less than 60.
print(marks[np.where(marks<60)])

# 18. Find all marks between 60 and 90, including both 60 and 90.
print(marks[np.where((marks>=60) & (marks<=90))])

# 19. Find the sales values that are greater than ■15,000.
print(sales[np.where(sales>15000)])

# 20. Count how many students scored more than 80.
print(np.size(marks[np.where(marks>80)]))

# 21. Replace all marks below 50 with 50.
marks=np.where(marks<50,50,marks)
print(marks)

# =================================================================
# Part E – Reshape & 2D Arrays

# 22. Create numbers = np.arange(1, 13) and reshape the array into a 3 × 4 matrix.

numbers=np.arange(1,13).reshape(3,4)
print(numbers)

# 23. From the 3 × 4 matrix, 
# print the first row, last row, first column, and last column.
print(numbers[0])

# last row, 
print(numbers[-1])

# first column, 
print(numbers[:,0])

# and last column.
print(numbers[:,3])

# 24. From the matrix, extract [[2, 3], [6, 7]] using slicing.
print(numbers[0:2,1:3])

# 25. Find the sum of each row and each column.
print(np.sum(numbers,axis=1))
print(np.sum(numbers,axis=0))


# =================================================================
# Bonus Questions

# 26. Sort the marks array in ascending order.
print(np.sort(marks))

# 27. Sort the sales array in descending order.
print(np.sort(sales)[::-1])

# 28. Find the index position of the student who scored the highest mark.
print(np.argmax(marks))

# 29. Find the index position of the student who has the lowest mark.
print(np.argmin(marks))


# 30. Calculate the difference between each student's mark and the average mark.
new=[np.average(marks)-marks]
print(new)
# 31. Find the unique values 
# from: arr = np.array([10, 20, 10, 30, 20, 40, 10, 50, 30]).
arr = np.array([10, 20, 10, 30, 20, 40, 10, 50, 30])
print(np.unique(arr))

# 32. Create an array of numbers from 1 to 50 
# and find all even numbers, all odd numbers, and numbers
# divisible by 5.

arr5=np.arange(1,50)
even=np.where(arr5 % 2 == 0)
print("even array",even)
odd=np.where(arr5 % 2 == 1)
print("odd array",odd)
print("divisible by 5",arr5[np.where(arr5%5==0)])

# 33. Create a 4 × 4 matrix containing numbers from 1 to 16
arr6=np.arange(1,17).reshape(4,4)
print(arr6)
#  and find its maximum value, minimum value,
print(np.max(arr6))
print(np.min(arr6))

# row-wise sum, and column-wise sum.
print(np.sum(arr6,axis=1))#row wise

print(np.sum(arr6,axis=0))#column wise


# 34. Create a = np.array([10,20,30,40,50]) and b = np.array([5,15,25,35,45]). Find addition, subtraction,
# multiplication, and division.

a = np.array([10,20,30,40,50])
b = np.array([5,15,25,35,45])


print(np.add(a,b))

print(np.subtract(a,b))

print(np.multiply(a,b))

print(np.divide(a,b))

# 35. Using marks, create a new array where marks ≥ 90 → Excellent, ≥ 75 → Good, ≥ 50 → Average, and
# < 50 → Needs Improvement.
marks = np.array([78, 65, 89, 45, 92, 56, 73, 88, 61, 95])
result=np.where(marks>=90,"Excellent",
       np.where(marks>=75,"good",
       np.where(marks>=50,"Average",
                "Needs Improvemen")))       
print(result)