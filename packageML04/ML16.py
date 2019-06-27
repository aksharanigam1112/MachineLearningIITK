import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_data(filename):

    file = pd.read_csv(filename)
    print(file)

    r, c = file.shape
    x_para = np.zeros([r])
    y_para = np.zeros([r])

    i = 0
    for single_sq_feet, single_price_value in zip(file['square_feet'], file['price']):

        if (i < r):
            x_para[i] = np.array(float(single_sq_feet))
            y_para[i] = float(single_price_value)
            i += 1

    # print("\n",x_para,"\n",y_para)
    return x_para, y_para


def estimate_coef(x, y):

    n = np.size(x)

    mx = np.mean(x)
    my = np.mean(y)

    ssxy = np.sum(x * y) - n * mx * my
    ssxx = np.sum(x * x) - n * mx * mx

    m = ssxy / ssxx

    c = my - m * mx
    return [m, c]


def plot_regression_line(x, y, ques, b):

    plt.scatter(x, y, color="c", marker="o", s=30)

    y_pred = b[0] + b[1] * x
    ans = b[0] + b[1] * ques

    plt.scatter(x,y_pred,color="r")
    plt.scatter(ques, ans, color="g")
    plt.plot(x, y_pred, color="b")
    plt.show()
    return ans


def main():
    x, y = get_data('LR_House_price.csv')
    ques = 700
    m, c = estimate_coef(x, y)
    ans = plot_regression_line(x, y, ques, [c, m])
    print("\nEstimated ans : ", ans)


if __name__ == "__main__":
    main()
