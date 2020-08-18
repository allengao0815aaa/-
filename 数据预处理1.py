#-*- coding:utf-8 -*-
# author:allen
# datetime:2020-05-31 11:05
# software: PyCharm
# environment:
# packages:

import numpy as np
import pandas as pd


df = pd.read_excel("干部简历信息整理表汇总.xlsx")
#print(df)

#得到各级干部平均年龄
df_avg_age = df.groupby("干部级别").mean()["年龄"]
avg_age =np.array(df_avg_age).tolist()
print(avg_age)

rank = np.array(df["干部级别"]).tolist()
age = np.array(df["年龄"]).tolist()

potential = []

#省部级副职（四级干部）及以上，全部为具有较高培养潜力干部；厅局（地）正职（五级干部）及以下，若年龄小于该级别平均年龄，则有较高培养潜力（用1表示），若年龄大于等于该级别平均年龄，则认为无较高培养潜力（用0表示）
for i in range(len(rank)):
    if (rank[i] > 4) & (age[i] >= avg_age[rank[i]-1]):
        potential.append(0)
    else:
        potential.append(1)

#print (potential)
df["培养潜力"] = potential

df.to_excel("干部信息整理预处理.xlsx",index = None)




