#%%
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("1-subset-covid-data.csv", encoding="utf-8")
df.head()
#%%
df.info()

# %%
df.deaths.value_counts()

# %%
data12042020 = df[df.date=="2020-04-12"]

print ("trung bình số ca mắc mới: " + str(data12042020.cases.mean()))
print ("trung vị của số ca mắc mới: "+ str(data12042020.cases.median()))
plt.hist(data12042020.cases, bins = 200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("số số ca mắc mới")
plt.ylabel("Số lượng quốc gia")
# %%
print("tổng số ca nhiễm và số ca ncủa các châu lục")
data12042020.groupby('continent')['cases','deaths'].sum()

# %%
print ("5 quốc gia có số ca nhiễm mới cao nhất")
df = df.sort_values('cases',ascending = False)
df.head(5)

# %%
print ("5 quốc gia có số ca tử vong cao nhất")
df = df.sort_values('deaths',ascending = False)
df.head(5)

# %%
