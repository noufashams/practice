import pandas as pd

# pd.Series(data)
# data   --> list/dictionary/tuple

# data=[1,2,3,4,5,6,7]

# series_1=pd.Series(data)
# print(series_1)

# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# 5    6
# 6    7
# dtype: int64


# creating the series using dictionary
# =======================================
# here key becomes the index and the values becomes data in series
data={"a":20,"b":30,"c":40,"d":50,"e":60,"f":70,"g":80,"h":90,"i":100}
result=pd.Series(data)
print(result)
# a    20
# b    30
# c    40
# d    50
# e    60
# dtype: int64

# methods and attributes
# ========================
print(result.ndim) #>>1
print(result.index) #Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print(result.shape) #(5,)
print(result.dtype) #int64
print(result.head()) #a    20
                     #b    30
                     #c    40
                     #d    50
                     #e    60
# extract last first values from series
                     #by default gives first five values 
                    #  if mentioned like 


print(result.head(3))
# a    20
# b    30
# c    40
# dtype: int64
# we get first 3 valuess

print(result.tail())
# e     60
# f     70
# g     80
# h     90
# i    100
# dtype: int64
# extract last few values from series

s1=pd.Series([1,2,3,4,5,6,7])
s2=pd.Series([8,9,10,11,12,13,14])

print(s1.add(s2))
# 0     9
# 1    11
# 2    13
# 3    15
# 4    17
# 5    19
# 6    21
# dtype: int64

print(s1.sub(s2))
# 0   -7
# 1   -7
# 2   -7
# 3   -7
# 4   -7
# 5   -7
# 6   -7
# dtype: int64


print(s1.multiply(s2))
# 0     8
# 1    18
# 2    30
# 3    44
# 4    60
# 5    78
# 6    98
# dtype: int64

print(s1.divide(s2))
# dtype: int64
# 0    0.125000
# 1    0.222222
# 2    0.300000
# 3    0.363636
# 4    0.416667
# 5    0.461538
# 6    0.500000
# dtype: float64

print(pd.concat([s1,s2]))
# 0     1
# 1     2
# 2     3
# 3     4
# 4     5
# 5     6
# 6     7
# 0     8
# 1     9
# 2    10
# 3    11
# 4    12
# 5    13
# 6    14
# dtype: int64