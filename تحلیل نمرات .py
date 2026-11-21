
import numpy as np

#ارایه نمرات
scores = np.array([12, 15, 18, 20, 9, 14, 17, 19, 8, 16])

#میانگین نمرات
average = np.mean(scores)

#پیدا کردن کوچیک و بزرگترین نمره
highest = np.max(scores)
lowest = np.min(scores)

#جمع تمام نمرات
total = np.sum(scores)

#پیدا کردن نمرات بزرگتر از 18
excellent = scores[scores > 18]#سام نزاریم مینویسشون

#پیدا کردن کسانی که افتادن یا پاس شدن
passed = np.sum(scores >= 10)#نمرات بزرگتر یا مساوی 10 پاس هستند فقط بشمارشون
failed = np.sum(scores < 10)#نمرات کمتر 10 افتادن

#پیام نمایشی
print("===== Student Score Analysis =====")

print("Scores:", scores)
print("Average:", average)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total scores:", total)
print("Excellent scores:", excellent)
print("Passed students:", passed)
print("Failed students:", failed)