
import numpy as np
from sklearn.linear_model import LinearRegression

# اطلاعات خانه ها
sizes = np.array([50, 60, 70, 80, 90, 100]).reshape(-1, 1)

# قیمت خانه ها
prices = np.array([1000, 1200, 1400, 1600, 1800, 2000])

# ساخت مدل
model = LinearRegression()

# آموزش مدل
model.fit(sizes, prices)

# خانه جدید
new_house = np.array([[75]])

# پیش بینی قیمت
prediction = model.predict(new_house)

# نمایش نتیجه
print("House size:", new_house[0][0])
print("Predicted price:", prediction[0], "million toman")
