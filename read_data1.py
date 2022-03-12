import pandas as pd
import numpy as np
data_dir = r"E:/code/pyrorch/QT/数据库/data/data1/mcpd模型数据汇总1011.xlsx"
data = pd.read_excel(data_dir,sheet_name="氨基酸模型",engine='openpyxl',header=1)
print(data)
# data = data.values.tolist()
# data = np.array(data)
# print(data["水"])
#

dic = {}

name = data.columns.tolist()
#print(name)
real_name = []

for i in name:
    if "氯丙醇" in i:
        real_name.append(i)
        break
    else:
        real_name.append(i)
#print(real_name)
#data.set_index(real_name[0:len(real_name)-1], inplace=True)
#data = data.loc[:,real_name[-1]]
for i in range(0,len(real_name)-1):
    data1 = data.loc[:,real_name[i]]
    data1 = data1.values.tolist()
    data1 = set(data1)
    data1 = list(data1)
    #print(data1)
    data1.sort()
    for j in data1:
        dic.setdefault(real_name[i],[]).append(j)
# print(dic)
# print(dic[real_name[3]])
    #
    # data.set_index(real_name[0:len(real_name)-1], inplace=True)
    # for i in range(len(real_name)-1):
    #     data = data.loc[dic[real_name[i]][0]]

# data = data.loc[dic[real_name[0]][0]]
# data = data.loc[dic[real_name[1]][0]]
# data = data.loc[dic[real_name[2]][0]]
# data = data.loc[1]
# data = data.loc[dic[real_name[4]][0]]
    # print("xxxxxxxxxxxxxxxxxxxxx\n",data[0])

# print("XXXXXXXXXXXXXXXXXXXXXXXX\n",data)


# data = data.values
# for i in range(0,len(name)):
#     if "U" in name[i]:
#         data = data[:,0:i]
#         break

# print(data[[name]])
# data1 = data[data.甘油酯种类=="三油酸甘油酯"]
# print(data1)

# a = []
# print(len(data))
# for i in range(1,len(data)):
#     print(type(data[1][1]))
#     break
#
# #     a.append(data[i][1])
# a = list(set(a))
# a.sort()
# print(a)


# xl = pd.read_excel(data_dir,engine='openpyxl',sheet_name=None)
# model_name = []
# for i in xl.keys():
#     print(i)
#     model_name.append(i)
# print(model_name)