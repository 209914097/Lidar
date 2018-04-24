# ---------------这是我迄今为止写过最简洁的代码，7行代码，干了4件事 1.筛选排序2.竖放变横放3.重新排序4.替换坏值-----------------------#

df1=pd.read_csv('kk.csv')
df1=df1[ ((312<df1['azimuth'])&(df1['azimuth']<360)) | ((0<df1['azimuth'])&(df1['azimuth']<48)) ].set_index('Unnamed: 0').sort_values(by='azimuth', ascending=False)#1.根据方位角范围筛选数据并排序
df3=DataFrame({'ID':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]},index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])[['ID']].set_index('ID')
for x in range(int(len(df1)/16)):# 2.竖着放的数据变为横着放
    df2=df1[x*16:(x+1)*16][['ID','y']].set_index('ID')
    df3=pd.concat([df3,df2],axis=1)
df3.reindex(index=[1,2,3,4,5,6,7,8,16,15,14,13,12,11,10,9]).replace(to_replace=[0],value='None').to_csv('df.csv')#3.古怪的重新排序 4.替换坏数据
