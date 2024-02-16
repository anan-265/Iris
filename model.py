#Importing Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the data
data=pd.read_csv("https://gist.github.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/aaecbd14aeaa468cd749528f291aa8a30c2ea09e/iris_dataset.csv")
#LabelEncoding

#Importing modules
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data["target"] = le.fit_transform(data["target"])

#Model training
from sklearn.model_selection import train_test_split
x = data.drop(columns="target")
y = data["target"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30)

#logistiic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)
