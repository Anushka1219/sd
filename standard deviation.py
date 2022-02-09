from collections import Counter
import pandas as pd
import plotly.express as px
import csv
import math

with open ("HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
heightdata=[]

for i in range(len(filedata)):
    num=filedata[i][1]
    heightdata.append(float(num))

n=len(heightdata)


   
total=0

for i in heightdata:
    total=total+i

mean=total/n
print(mean)


df=pd.read_csv("HeightWeight.csv")
print(df)
fig=px.scatter(df,x="Index", y="Height", title="Height Data")
fig.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=n)])
fig.show()

SDlist=[]

for i in heightdata:
    i=i-mean
    SDlist.append(i)


squarelist=[]

for i in SDlist:
    i=i**2
    squarelist.append(i)


sum=0
for i in squarelist:
    sum=sum+i

print(sum)

result=sum/len(heightdata)-1

print(result)

sd=math.sqrt(result)
print(sd)

