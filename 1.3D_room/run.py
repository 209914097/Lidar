from capture import *
from dataprocessing import *
from drawing import *
import pandas as pd
import os

input('调整至0°按回车键继续')
print('处理中...')
dpkt = sniff(filter="udp and ip src 192.168.1.200 and udp port 6699", count=83,
                 prn=lambda x: ok(hexdump(x[0][Raw].load, dump=True)))
rotation(0,'M.csv')
os.remove('kk.csv')


input('调整至-25°按回车键继续')#沿着传感器Y轴负方向看，后仰时角度输入为负数，与IO-Motor角度定义相反。
print('处理中...')
dpkt = sniff(filter="udp and ip src 192.168.1.200 and udp port 6699", count=83,
                 prn=lambda x: ok(hexdump(x[0][Raw].load, dump=True)))
rotation(-25,'H.csv')
os.remove('kk.csv')


input('调整至25°按回车键继续')#沿着传感器Y轴负方向看，前倾时角度输入为正数，与IO-Motor角度定义相反。
print('处理中...')
dpkt = sniff(filter="udp and ip src 192.168.1.200 and udp port 6699", count=83,
                 prn=lambda x: ok(hexdump(x[0][Raw].load, dump=True)))
rotation(25,'L.csv')
os.remove('kk.csv')

# ---------------合并数据-----------------------#
pd.concat([pd.read_csv('H.csv').set_index('Unnamed: 0'),pd.read_csv('M.csv').set_index('Unnamed: 0'),pd.read_csv('L.csv').set_index('Unnamed: 0')],axis=0).to_csv('intergrate.csv')
# ---------------画图-----------------------#
show()
