import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model  # ScientificKit for Machine Learning
import warnings

warnings.filterwarnings(action="ignore")

# Function to get data
def get_data(filename):
    dataframe = pd.read_csv(filename)
    print(dataframe)

    x_para = []
    y_para = []

    # Zip function combines the the data together so that it is able to cut the data into pieces
    # For the file we have uni-variant input
    # Bit keep the format [ [ ] , ... ] for input be it any type

    for single_sq_feet, single_price_value in zip(dataframe['square_feet'], dataframe['price']):

        x_para.append([float(single_sq_feet)])
        y_para.append(float(single_price_value))

    return x_para, y_para


# Functions for fitting data to linear model

def linear_model_main(x_para, y_para, quest_value):

    # Create linear reg object
    regr = linear_model.LinearRegression()  # loading the code of the class LinearRegression

    print("Area : ", x_para)
    print("Price : ", y_para)

    regr.fit(x_para, y_para)        # Fitting the training data to calculate the best fit hypothesis parameters (m,c)

    pred_ans = regr.predict([[quest_value]])        # Getting the ans for question on the trained algo
    predictions = {}

    predictions['coefficient'] = regr.coef_     # m
    predictions['intercept'] = regr.intercept_  # c
    predictions['predicted_ans'] = pred_ans     # ans corresponding to the ques i.e 700 sq feet

    print("\nOutput from the Machine : ", pred_ans)
    plt.scatter(x_para, y_para, color="m", marker='o', s=30)

    all_pred_y = regr.predict(x_para)           # Predicting y' for all the x_para values
    # plt.scatter(x_para, all_pred_y, color="b")
    plt.plot(x_para, all_pred_y, color="r")

    plt.scatter(quest_value, pred_ans, color="g")

    plt.show()

    return predictions


if __name__ == "__main__":
    x, y = get_data('LR_House_price.csv')
    ques_value = 700  # Predicting the house price for a 700 sq feet area
    result = linear_model_main(x, y, ques_value)

    print("\nIntercept value = ", result['intercept'])
    print("\nCoefficient = ", result['coefficient'])
    print("\nPredicted house price value = ", result['predicted_ans'])
