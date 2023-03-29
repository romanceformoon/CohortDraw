import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

START_WEEK = 9
END_WEEK = 13


def w_cohort(df, n):
    w_0 = len(df["user_id"][df["week"] == n].unique())
    w_co_list = [w_0]
    r_list = [(w_0 / w_0) * 100]
    w_cohort_rate_df = pd.DataFrame()
    for i in range(n + 1, END_WEEK + 1):
        w_cohort = len(
            df["user_id"][
                (df["user_id"].isin(df["user_id"][df["week"] == n].unique()))
                & (df["week"] == i)
            ].unique()
        )
        w_co_list.append(w_cohort)
        rate = round((w_co_list[i - n] / w_0) * 100, 2)
        r_list.append(rate)
        w_cohort_rate_df = pd.DataFrame(r_list).T

    return w_cohort_rate_df


data = pd.read_csv("test.csv")
data = data.dropna()

w_9 = w_cohort(data, 9)
w_10 = w_cohort(data, 10)
w_11 = w_cohort(data, 11)
w_12 = w_cohort(data, 12)
w_13 = w_cohort(data, END_WEEK)

c = w_9.append(w_10)
c = c.append(w_11)
c = c.append(w_12)
c = c.append(w_13).fillna(0).reset_index()

cohort = c.drop(columns=["index", 0])
cohort.index = np.arange(1, len(cohort) + 1)

print(cohort)

ax = sns.heatmap(cohort, annot=True, fmt="f")

plt.title("Cohort Retention Rate(W) [2023/3/3 ~ 2023/3/28]", fontsize=14)

plt.show()
