import pandas as pd

data={
    "name":["akhil","meera","rahul","arun"],
    "age":[25,28,30,31],
    "dept":["it","hr","testing","hr"],
    "salary":[10000,20000,17000,25000]
}

result=pd.DataFrame(data)
print(result)

#     name  age     dept  salary
# 0  akhil   25       it   10000
# 1  meera   28       hr   20000
# 2  rahul   30  testing   17000
# 3   arun   31       hr   25000
print(result.head())
"""     name  age     dept  salary
0  akhil   25       it   10000
1  meera   28       hr   20000
2  rahul   30  testing   17000
3   arun   31       hr   25000

returns first few lines of the data frame
"""
print(result.tail())
"""
    name  age     dept  salary
0  akhil   25       it   10000
1  meera   28       hr   20000
2  rahul   30  testing   17000
3   arun   31       hr   25000
returns last few lines of the dataframe
"""

print(result.shape)
(4, 4)

print(result.columns) #Index(['name', 'age', 'dept', 'salary'], dtype='object')
# returns column names from data frame

result.columns=['Name', 'Age', 'Dept', 'Salary']
# update column names

result["Place"]=["kochi","tvm","alappy","chennai"]
print(result)

"""
    Name  Age     Dept  Salary    Place
0  akhil   25       it   10000    kochi
1  meera   28       hr   20000      tvm
2  rahul   30  testing   17000   alappy
3   arun   31       hr   25000  chennai
"""

print(result.describe())
# returns the statistical summary of the dataframe that contains the numerical values

print(result["Place"])
# 0      kochi
# 1        tvm
# 2     alappy
# 3    chennai
# Name: Place, dtype: object

print(result["Age"])
# 0    25
# 1    28
# 2    30
# 3    31
# Name: Age, dtype: int64

print(result.sort_values(by="Age",ascending=False))
#     Name  Age     Dept  Salary    Place
# 3   arun   31       hr   25000  chennai
# 2  rahul   30  testing   17000   alappy
# 1  meera   28       hr   20000      tvm
# 0  akhil   25       it   10000    kochi


print(result.sample())
#  Name  Age     Dept  Salary    Place
# 3   arun   31       hr   25000  chennai
# 2  rahul   30  testing   17000   alappy
# 1  meera   28       hr   20000      tvm
# 0  akhil   25       it   10000    kochi
#     Name  Age     Dept  Salary   Place
# 2  rahul   30  testing   17000  alappy


print(result.dtypes)
# Name      object
# Age        int64
# Dept      object
# Salary     int64
# Place     object
# dtype: object


print(result.columns)
# Index(['Name', 'Age', 'Dept', 'Salary', 'Place'], dtype='object')