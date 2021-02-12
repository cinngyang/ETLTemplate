from myLib import dbconnect as dbcn 
import pandas as pd


cn=dbcn.dbConnect()
cn.mySqlCon(cn.pi,'Testdb')
strSql="select * from Testdb.turnrate"
df=cn.mySqlQuer(cn.pi,'Testdb',strSql)
print(df.shape)

df=pd.DataFrame({'rot_date':['2021/02/11','2021/02/11'],
'inv_age':['10-20','20-30'],
'item_value':[6381,1276],
'unit':['AT','AT'],
'update_time':['2021/02/11 21:41' ,'2021/02/11 21:41']})

ret=cn.mySqlInsDataFrame(cn.pi,'Testdb','turnrate',df)




