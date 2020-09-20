import pandas as pd # importing pandas property
# Data source: https://drive.google.com/file/d/17j5y4WwS6xpcANlESb24FzyR7Vrzam65/view
data = pd.read_csv("policedata.csv")  # read the file using pandas
print(data) # test to print data
# Task 1: Remove the column that only contains missing values
data.isnull().sum()
data.drop(columns = "country_name", inplace = True)
# Task 2: For speeding, were women or men stopped more often?
data.head()
data[data.violation == 'Speeding'].driver_gender.value_counts()
# Task 3: Does gender affect who gets searched during a stop?
data.head()
data.groupby("driver_gender").search_conducted.sum()
data.search_conducted.value_counts()
# Task 4: What is the mean stop_duration?
data.head()
data.stop_duration.value_counts()
data["stop_duration"] = data["stop_duration"].map({'0-15 min': 7.5, '16-30 min' : 24, '30 + min' : 45})
data["stop_duration"].mean()
# Task 5: Compare the age distributions for each violation
data.head()
data.groupby("violation").driver_age.describe()

















