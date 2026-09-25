# machine learning
# ===================

# machine learning >>> enables machine to learn patterns from 
# data and make decisions or predictions without being programmed

# 3 types of machine learning
# ============================

# 1)supervised learning
# ======================
# type of machine learning in which a model learns from labeled data 
# where thr input and expected output are provided during training
# Eg:weather prediction

# there are 2 types of supervised learning:

# i)Classification
# ==================
# classification is a type of supervised learning used to predict a category
# eg:Iris,disease classificaton


# ii)Regression
# ================
# regression is a type of supervised learning used to predict the continuous numerical value
# eg:house price,temperature,sale prediction

# ALGORITHMS
# ============
# algorithms are used to train machine
# Different types of algorithms:
# ================================

# 1)KNN-K nearest neighbour >>> classification,regression
# ===========================
# A supervised machine learning algorithm that predicts the output of a new point
# looking at its nearest data point in the training dataset

# | Student | Hours Studied | Attendance | Result |
# | --------|---------------|------------|--------|
# | A       |        1      |       50   |   Fail |
# | B       |        2      |       55   |   Fail |
# | C       |        3      |       60   |   Fail |
# | D       |        5      |       75   |   Pass |
# | E       |        6      |       80   |   Pass |
# | F       |        7      |       90   |   Pass |

# new pint G(5,78) (x1,y1)
# first point A(1,50) (x2,y2)

# Euclidean Distance formula
# ==========================
# sqrt((x2-x1)^2+(y2-y1^2))

# sqrt((1-5)^2+(50-78)^2)

# suppose the distance calculated are :
# 28.28,23.19,18.11,3,2.23,12.16
# arranges them in ascending order:
# 3,2.23,12.16,18.11,23.19,28.28


# if we give k=5:
# 0.5,1.3,2.4,2.5,2.9
# pass,pass,fail,fail,pass
# it chooses pass as the majority is pass
# pass count=3
# fail count=2

# k=3
# it chooses 3 of them and chooses the majority
# # 0.5,1.3,2.4
# # pass,pass,fail


# classification algorithms:
# ==========================
# KNN             >>> Distance Formula|..
# Naive bayse     >>> Probability(weather)
# Decision Tree   >>> 
# Random Forest   >>>(best)
# Xg boosting     >>>

# Regression Algorithms
# ======================
# Linear Regression
# Polynomial












# 2)Unsupervised learning
# ========================
# Type of learning where the machine learns the pattern from data
# without the expected output
# eg:customer segmentation(which kind of people purchase at what time of the month)


# 3)reinforcement learning
# ========================

