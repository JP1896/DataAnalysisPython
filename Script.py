import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import functions as fun

#---------------------EXCEL------------------------
df = pd.read_csv('SampleData.csv')
print('The General Data Frame is : \n ',df)
df2 = pd.read_csv('SampleData2.csv')
print('The Second data frame is : \n',df2)
df3 = pd.read_csv('SampleData3.csv')
print('The Third data frame is : \n ',df3)
df4 = pd.read_csv('SampleData4.csv')
print('The Fourth data frame is : \n',df4)

'''
---------------------------------------------------Query to the First dataframe---------------------------------------------------
'''
#DIVIDED BY REGIONS, EAST, CENTRAL AND WEST
df_query_east = df.query("Region == 'East'")
#print(df_query_east)
df_query_central = df.query("Region == 'Central'")
#print(df_query_central)
df_query_west = df.query("Region == 'West'")
#print(df_query_west)
'''
---------------------------------------------------Query in the second data frame---------------------------------------------------
'''
df2_query_date = df2["OrderDate"].to_list()
#print(df2_query_date)
df2_query_units = df2["Units"].to_list()
#print(df2_query_units)
df2_query_income = df2["Income"].to_list()
#print(df2_query_income)
'''
---------------------------------------------------Query in the third data frame---------------------------------------------------
'''
print('---------------------------------------------------DATA FOR 2019---------------------------------------------------')
df3_query_date = df3["OrderDate"].to_list()
#print(df3_query_date)
df3_query_units = df3["Units"].to_list()
#print(df3_query_units)
df3_query_income = df3["Income"].to_list()
#print(df3_query_income)
df3_total_units = sum(df3_query_units)
df3_total_profit = sum(df3_query_income)
print('Total units Sold in 2019: ', df3_total_units)
print('Profit in 2019: ','$', df3_total_profit)
'''
---------------------------------------------------Query in the fourth data frame---------------------------------------------------
'''
print('---------------------------------------------------DATA FOR 2020---------------------------------------------------')
df4_query_date = df4["OrderDate"].to_list()
#print(df4_query_date)
df4_query_units = df4["Units"].to_list()
#print(df4_query_units)
df4_query_income = df4["Income"].to_list()
#print(df4_query_income)
df4_total_units = sum(df4_query_units)
df4_total_profit = sum(df4_query_income)

print('Total units Sold in 2020: ', df4_total_units)
print('Profit in 2020: ', '$',df4_total_profit)

'''
From the regions we need to get the total amount of units sold
'''
df_query_east_units = df_query_east["Units"].to_list()
te = sum(df_query_east_units)
#print('EAST UNITS : ',te)
df_query_central_units = df_query_central["Units"].to_list()
tc = sum(df_query_central_units)
#print('CENTRAL UNITS : ',tc)
df_query_west_units = df_query_west["Units"].to_list()
tw = sum(df_query_west_units)
#print('WEST UNITS : ',tw)
'''
DIVIDED BY ITEMS, PENCIL, BINDER, PEN, DESK, PEN SET
'''
df_query_pencil = df.query("Item == 'Pencil'")
#print(df_query_pencil)
df_query_binder = df.query("Item == 'Binder'")
#print(df_query_binder)
df_query_pen = df.query("Item == 'Pen'")
#print(df_query_pen)
df_query_desk = df.query("Item == 'Desk'")
#print(df_query_desk)
df_query_penset = df.query("Item == 'Pen Set'")
#print(df_query_penset)
'''
Transform each column from the data frame to a list, this will make much easier to manipulate the data to graph 
or perform further analysis
'''
#Creating lists of columns (GENERAL LEVEL)
Date_list = df["OrderDate"].to_list()
#print(Date_list)
Region_list = df["Region"].to_list()
#print(Region_list)
Rep_list = df["Rep"].to_list()
#print(Rep_list)
Item_list = df["Item"].to_list()
#print(Item_list)
Units_list = df["Units"].to_list()
#print('Total units sold: ', sum(Units_list))

'''
filtering information from the previous query of each item, in this case it's used to get the total amount of
units sold, this will be for a pie chart
'''
df_query_pencil_units = df_query_pencil["Units"].to_list()
#print("Pencil units sold: ", sum(df_query_pencil_units))
df_query_binder_units = df_query_binder["Units"].to_list()
#print("Binder units sold: ", sum(df_query_binder_units))
df_query_pen_units = df_query_pen["Units"].to_list()
#print("Pen units sold: ", sum(df_query_pen_units))
df_query_desk_units = df_query_desk["Units"].to_list()
#print("Desk units sold: ", sum(df_query_desk_units))
df_query_penset_units = df_query_penset["Units"].to_list()
#print("Pen Set units sold: ", sum(df_query_penset_units))
#----------------------------------------------------Pie Chart----------------------------------------------------------
mylabels = 'Pencil','Binder','Pen','Desk','Pen Set'
sizes = [sum(df_query_pencil_units),sum(df_query_binder_units),sum(df_query_pen_units),sum(df_query_desk_units),sum(df_query_penset_units)]
explode = (0,0.1,0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=mylabels, autopct='%1.1f%%',
            startangle=90)

ax1.axis('equal')
plt.title('Items Sold \n' + '2019 - 2020')
plt.show()
#-----------------------------------------------Plot the three regions------------------------------
labels = ['East', 'Central', 'West']
units = [te,tc,tw]
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/32,units,width,label='Units Sold')
#Adding format to graph
ax.set_ylabel('Units')
ax.set_title('Units sold by region')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.bar_label(rects1, padding=3)
fig.tight_layout()
plt.show()
#-----------------------------------------------Line graphs----------------------------------
plt.plot(df2_query_date,df2_query_units)
plt.title('Sales \n' + '2019-2020')
plt.xlabel('Date')
plt.ylabel('Units')
plt.show()

plt.plot(df2_query_date,df2_query_income)
plt.title('Profits \n' + '2019-2020')
plt.xlabel('Date')
plt.ylabel('USD - $')
plt.show()

'''
Analyzing main differences between both years 
It's important to notice that we are gonna get different values depending the way we analyze things, 
it's not the same analyze from original to 2019 than 2019 to original.
'''



#Constants
originalUnits = 800
originalProfits = 10000

print('\n-------------------Original values vs 2019 values-------------------\n')
fun.compareDataUnits(originalUnits,df3_total_units)    # 800 - 1178
fun.compareDataUnits(originalProfits,df3_total_profit) # 10000 - 9258.34
print('\n-------------------2019 values vs Original Values -------------------\n')
fun.compareDataUnits(df3_total_units,originalUnits)    # 1178 - 800
fun.compareDataUnits(df3_total_profit,originalProfits) # 9258.34 - 100000


print('\n-------------------Original values vs 2020 values-------------------\n')
fun.compareDataUnits(originalUnits,df4_total_units)    # 800 - 943
fun.compareDataUnits(originalProfits,df4_total_profit) # 10000 - 10369.54
print('\n-------------------2020 values vs Original Values -------------------\n')
fun.compareDataUnits(df4_total_units,originalUnits)    # 943 - 800
fun.compareDataUnits(df4_total_profit,originalProfits) # 9258.34 - 100000



print('\n-------------------2019 values vs 2020 values-------------------\n')
fun.compareDataUnits(df3_total_units,df4_total_units)  #1178 - 943
fun.compareDataUnits(df3_total_profit,df4_total_profit)#9258.34 - 10369.54
print('\n-------------------2020 values vs 2019 values-------------------\n')
fun.compareDataUnits(df4_total_units,df3_total_units)  #943 - 1178
fun.compareDataUnits(df4_total_profit,df3_total_profit)#10369.54 - 49258.34