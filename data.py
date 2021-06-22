import plotly.figure_factory as ff
import pandas as pd
import csv 
import math
import statistics
df = pd.read_csv('data.csv')
heightList=df["Height(Inches)"].to_list()

height_mean=statistics.mean(heightList)
height_mode=statistics.mode(heightList)
height_stnd=statistics.stdev(heightList)
height_median=statistics.median(heightList)

hstndstart1,hstndend1=height_mean-height_stnd,height_mean+height_stnd
hstndstart2,hstndend2=height_mean-(2*height_stnd),height_mean+(2*height_stnd)
hstndstart3,hstndend3=height_mean-(3*height_stnd),height_mean+(3*height_stnd)

h1_result=[result for result in heightList if result>hstndstart1 and result<hstndend1]
h2_result=[result for result in heightList if result>hstndstart2 and result<hstndend2]
h3_result=[result for result in heightList if result>hstndstart3 and result<hstndend3]

print(len(h1_result)*100/len(heightList),"percent of data lies in first standard deviation")
print(len(h2_result)*100/len(heightList),"percent of data lies in second standard deviation")
print(len(h3_result)*100/len(heightList),"percent of data lies in third standard deviation")



