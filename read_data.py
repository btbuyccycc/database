import pandas as pd

class read_data():
    def __init__(self):
        super(read_data, self).__init__()
        self.MPCD_dir = r"mcpd模型数据汇总1011.xlsx"
        self.MPCDE_dir = r"MCPDE模型数据汇总1011.xlsx"

    def huoqu_zucheng(self, model,leibie):
        real_name = []
        dic = {}
        if leibie == "MCPD":
            data = pd.read_excel(self.MPCD_dir, sheet_name=model, header=1, engine='openpyxl')
        else:
            if model == "食品模型-炸土豆":
                data = pd.read_excel(self.MPCDE_dir, sheet_name=model, header=2, engine='openpyxl')
            else:
                data = pd.read_excel(self.MPCDE_dir, sheet_name=model, header=1, engine='openpyxl')
        zucheng = data.columns.tolist()

        for i in zucheng:
            if "氯丙醇" in i:
                real_name.append(i)
                break
            else:
                real_name.append(i)

        for i in range(0, len(real_name) - 1):
            data1 = data.loc[:, real_name[i]]
            data1 = data1.values.tolist()
            data1 = set(data1)
            data1 = list(data1)
            data1.sort()
            for j in data1:
                j = str(j)
                dic.setdefault(real_name[i], []).append(j)
        return real_name, dic

    def jieguochazhao(self,model,tiaojian,leibie):

        if leibie == "MCPD":
            data1 = pd.read_excel(self.MPCD_dir, sheet_name=model, header=1, engine='openpyxl')
        else:
            if model == "食品模型-炸土豆":
                data1 = pd.read_excel(self.MPCDE_dir, sheet_name=model, header=2, engine='openpyxl',usecols=[0,1,2,3])
            else:
                data1 = pd.read_excel(self.MPCDE_dir, sheet_name=model, header=1, engine='openpyxl')
        name = data1.columns.tolist()

        real_name = []

        for i in name:
            if "氯丙醇" in i:
                real_name.append(i)
                break
            else:
                real_name.append(i)

        if model == "食用油模型" or model == "食品模型-炒豇豆":
            data1.set_index(real_name[0:len(real_name) - 3], inplace=True)
        # elif model == "食品模型-炸土豆":
        #     data1.set_index(real_name[0:len(real_name) - 5], inplace=True)
        else:
            data1.set_index(real_name[0:len(real_name)-1], inplace=True)

        for i in range(len(tiaojian)):

            if i > 0:
                data1 = data1.loc[float(tiaojian[i])]
            else:
                if model == "食品模型-炸土豆":
                    data1 = data1.loc[float(tiaojian[i])]
                else:
                    data1 = data1.loc[(tiaojian[i])]

        if model == "食品模型-炒豇豆" or model == "食用油模型":
            return data1[0],data1[1],data1[2]


        return (data1[0])

if __name__ == "__main__":
    r1 =read_data()
    tiaojian = ['半乳糖', '0.01', '0.1', '1', '120', '1']
    #r1.jieguochazhao(tiaojian=tiaojian)