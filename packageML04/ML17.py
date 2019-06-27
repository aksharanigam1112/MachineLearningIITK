import pandas as pd
from sklearn import linear_model


def get_data(filename):
    data = pd.read_csv(filename)
    flash_x = []
    flash_y = []
    got_x = []
    got_y = []

    for x1, y1, x2, y2 in zip(data['Flash_episode_number'], data['Flash_us_viewers'], data['GoT_episode_number'],
                              data['GoT_us_viewers']):
        flash_x.append([float(x1)])
        flash_y.append(float(y1))
        got_x.append([float(x2)])
        got_y.append(float(y2))

    return flash_x, flash_y, got_x, got_y


# Function to predict the viewers of TV shows

def find_more_viewers(x1, y1, x2, y2):
    regr1 = linear_model.LinearRegression()
    regr1.fit(x1, y1)                   # Train the machine for Flash episode
    pred_val1 = regr1.predict([[10]])
    print("\nPrediction of Flash : ", pred_val1)

    regr2 = linear_model.LinearRegression()
    regr2.fit(x2, y2)                    # Train the machine for GoT episode
    pred_val2 = regr2.predict([[10]])
    print("\nPrediction of GoT : ", pred_val2)

    if (pred_val1 > pred_val2):
        print("\nNext episode of Flash TV show will have more viewers for the next Week ")
    else:
        print("\nNext episode of GoT TV show will have more viewers for the next Week ")


if __name__ == "__main__":
    x1, y1, x2, y2 = get_data('LR_Episodes.csv')

    find_more_viewers(x1, y1, x2, y2)
