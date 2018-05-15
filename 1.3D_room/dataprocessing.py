import pandas as pd
from numpy import *
import math

# # ---------------3D点云旋转坐标转换-----------------------#
def rotation(theta,filename):
    h=0.107   #激光头坐标原点与步进电机转轴距离
    theta=theta
    inv_R=array([[cos(math.radians(theta)),sin(math.radians(theta))],[-sin(math.radians(theta)),cos(math.radians(theta))]])#旋转矩阵R(θ)的逆矩阵,水平θ为0，俯向时θ为正，仰向时θ为负
    df1=pd.read_csv('kk.csv').set_index('Unnamed: 0')
    df1=df1[df1['dis']!=0]
    df1[['z']]=df1[['z']]+h
    df1[['y','z']]=dot(inv_R,df1[['y','z']].values.T).T
    df1.to_csv(filename)

