import pandas as pd
from model import SHEET_NAME
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_dict = pd.read_excel('测试数据.xlsx', sheet_name=SHEET_NAME)
# , index_col='算法'

df1 = data_dict[SHEET_NAME[0]]
df2 = data_dict[SHEET_NAME[1]]
df3 = data_dict[SHEET_NAME[2]]
df4 = data_dict[SHEET_NAME[3]]

print(df1)
# df = merge(merge(merge(df1, df2, how='outer'), df3, how='outer'), df4, how='outer')
#
# df.ix[df['key'] == 'PSONN','xpos'] = 1
# df.ix[df['key'] == 'GANN','xpos'] = 2
# df.ix[df['key'] == 'CPNN','xpos'] = 3
# df.ix[df['key'] == 'BASNN','xpos'] = 4
#
# print(df)


df1['训练错误率'] = df1['训练错误率'] * 100
df1['测试错误率'] = df1['测试错误率'] * 100
df4['训练错误率'] = df4['训练错误率'] * 100
df4['测试错误率'] = df4['测试错误率'] * 100

print(df4[['训练错误率', '测试错误率', '连接数', '运行时间']])

xpos = [1, 1, 1, 1,
        2, 2, 2, 2,
        3, 3, 3, 3,
        4, 4, 4, 4,
        1, 1, 1, 1,
        2, 2, 2, 2,
        3, 3, 3, 3,
        4, 4, 4, 4,
        ]

ypos = [1, 2, 3, 4,
        1, 2, 3, 4,
        1, 2, 3, 4,
        1, 2, 3, 4,
        1.5, 2.5, 3.5, 4.5,
        1.5, 2.5, 3.5, 4.5,
        1.5, 2.5, 3.5, 4.5,
        1.5, 2.5, 3.5, 4.5,

        ]

zpos = [0]
dx = [0.5]
dy = [0.5]
dz = []
for xl, cs, lj, yx in zip(df1['训练错误率'], df1['测试错误率'], df1['连接数'], df1['运行时间']):
    dz.append(xl)
    dz.append(cs)
    dz.append(lj)
    dz.append(yx)
for xl, cs, lj, yx in zip(df4['训练错误率'], df4['测试错误率'], df4['连接数'], df4['运行时间']):
    dz.append(xl)
    dz.append(cs)
    dz.append(lj)
    dz.append(yx)

print(xpos)
print(ypos)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
color = ['#668B8B', '#668B8B', '#668B8B', '#668B8B',
         '#54FF9F', '#54FF9F', '#54FF9F', '#54FF9F',
         '#FFF68F', '#FFF68F', '#FFF68F', '#FFF68F',
         '#FF4040', '#FF4040', '#FF4040', '#FF4040',
         '#00868B', '#00868B', '#00868B', '#00868B',
         '#008B00', '#008B00', '#008B00', '#008B00',
         '#FFC125', '#FFC125', '#FFC125', '#FFC125',
         '#8B2323', '#8B2323', '#8B2323', '#8B2323',
         ]
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=color, zsort='average')
ax.set_title('PSONN&BASNN')

plt.show()
