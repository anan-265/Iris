import sys
import warnings
warnings.filterwarnings('ignore')
from model import model
from model import le
while True:
    x = [[]]
    x[0].append(float(input("Enter Sepal Length in Centimeters\n")))
    x[0].append(float(input("Enter Sepal Width in Centimeters\n")))
    x[0].append(float(input("Enter Petal Length in Centimeters\n")))
    x[0].append(float(input("Enter Petal Width in Centimeters\n")))
    prediction = model.predict(x)
    binomial_name = le.inverse_transform(prediction)
    binomial_name = binomial_name[0]
    separator = binomial_name.index('-')
    genus = binomial_name[0:separator]
    specific_name = binomial_name[separator+1:]
    print("Species for the given input:", genus,specific_name)
    if input("Press Enter directly to exit, or press any key and press enter to perform a new operation\n") == "":
            sys.exit()