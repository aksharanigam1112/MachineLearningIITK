import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
    n = np.size(x)  # No. of observations

    # Mean of x & y vectors
    m_x = np.mean(x)
    m_y = np.mean(y)

    # Calculating cross deviation and deviation about x & y
    ss_x = np.sum(x * y) - n * m_x * m_y
    ss_y = np.sum(x * x) - n * m_x * m_x

    # Calculating regression coeff
    m = ss_x / ss_y
    c = m_y - m * m_x
    return [m, c]


def plot_regression_line(x, y, b):
    # PLotting the actual points
    plt.scatter(x, y, color="m", marker="o", s=30)      # m means Magenta,o means the way the dot appears s=30 means 30 pixel size

    # Predicted response vector
    y_pred = b[0] + b[1] * x  # y = mx + c

    # PLotting the regression line
    plt.scatter(x, y_pred, color="g")       # Points are formed
    plt.plot(x, y_pred, color="b")          # Line is formed over these points

    # putting lables
    plt.xlabel('x')
    plt.ylabel('y')

    # Function to show plot
    plt.show()


def main():
    # Observations
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    # Estimating the coeff
    m, c = estimate_coef(x, y)
    print("\nEstiamted coefficients : -")
    print("\nslope m = ", m)
    print("\ny-intercept = ", c)

    # PLotting the regression line
    plot_regression_line(x, y, [c, m])


if __name__ == "__main__":
    main()
