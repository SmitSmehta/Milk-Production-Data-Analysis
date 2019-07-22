#Final Project
#Em624 Informatics for Engineering Management
#Smit Mehta



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_excel("C:\Smit\Stevens College\First Sem\Em 624  Python\Project\Farmer\updated farmer sheet.xlsx")
df.head()

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:3.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
 
#Total Amount received to farmer
print ''
print'Total Amount received by all farmers are :- '
total_amount = df["Amount"].sum() 
print 'Total amount in rupees : ---- ',total_amount
print '\n'

#Minimum and Maximum amount received to a farmer 
print ''
print'Minimum and Maximum  Amount recieved to a farmers are : ---'
print 'Min:-- ',df["Amount"].min(),'\t Max:----',df["Amount"].max()

#Total Milk reproduce by farmers of village
df['Qty'] = pd.to_numeric(df['Qty'].str.replace(' ',''), errors='force')         #Converting Qty column object to float for summation
print''
print 'Total Milk Reproduce by farmers is :- '
total_qty = df['Qty'].sum()
print '',total_qty,'ltrs' 
 
#Minimum and Maximum milk produce by farmer  
print ''
print'Minimum and Maximum  MILK produce by a farmers are : ---'
print 'Min:-- ',df[df['Qty'] == df['Qty'].min()].head(5)[['Member Name','Qty']],'\n Max:----',df[df['Qty'] == df['Qty'].max()].head(5)[['Member Name','Qty']]

#Changing the time column to date time format
df['Time'] = pd.to_datetime(df['Time'])
df.head()
#print df.dtypes
        

#Names of the farmer Who received mimum amount of rupees

print ''
print 'Names of the farmers Who recieved minimum amount of rupees :---'
print df[df['Amount'] == df['Amount'].min()].head(5)[['Member Name','Amount','Time']]


#Names of the farmer Who received mimum amount of rupees   
print '\n'
print 'Names of the farmers Who recieved Maximum amount of rupees :---'
print df[df['Amount'] == df['Amount'].max()].head(5)[['Member Name','Amount','Time']]


print'\n'
#print df[df["Sex"] == "M"].head(5000)[['Member Name']]



#Counting Number of males and females
Male_Count = df[df['Sex'] == 'M'].count()['Member Name']
Female_count = df[df['Sex'] == 'F'].count()['Member Name']
print 'Total Numbers of Females are :-  ',Female_count,'\nTotal Number of males are :- ',Male_Count

#Creating Pie chart for males and females
plt.figure()
label = ['Male Farmers','Female Farmers']
y = [Male_Count,Female_count]
plt.pie(y,labels = label,autopct= make_autopct(y))
plt.legend(label,loc = 3)
plt.title('Male/Female Farmers')  #main title for the subplot
plt.axis('equal')


#Counting Number of Cow and buffalo Milk
print ''
Cow_milk_Count = df[df['Milk type'] == 'C'].count()['Member Name']
Buffalo_milk_count = df[df['Milk type'] == 'B'].count()['Member Name']
print 'Production of Cow milk  :-  ',Cow_milk_Count,'\nProduction of Buffalo Milk :- ',Buffalo_milk_count


#Creating Pie chart Cow and buffalo Milk
plt.figure()
Label = ['Cow Milk','Buffalo Milk']
x = [Cow_milk_Count,Buffalo_milk_count]
colors = ['skyblue','yellow']
plt.pie(x,labels = Label,colors = colors,autopct= make_autopct(x))
plt.legend(Label,loc = 3)
plt.title('Cow/Buffalo Milk')  #main title for the plot
plt.axis('equal')



#Males who produce Cow/Buffalo Milk
print''
print ''
M_C_Milk = df[(df["Sex"]=='M') & (df["Milk type"] == 'C')].count()['Member Name']
M_B_Milk = df[(df["Sex"]=='M') & (df["Milk type"] == 'B')].count()['Member Name']
print 'Males who produce Cow milk ',M_C_Milk,' \nMales who produce Buffalo milk',M_B_Milk

#Chart for Male producing buffalo and Cow milk
plt.figure()
Lab = ['Cow Milk(Male)','Buffalo Milk(Male)']
a = [M_C_Milk,M_B_Milk]
plt.pie(a,labels = Lab,autopct= make_autopct(a))
plt.legend(Lab,loc = 3)
plt.title('Cow/Buffalo Milk produce by Male Farmer')  #main title for the plot
plt.axis('equal')

#Females who produce Cow/Buffalo Milk
print''
print ''
F_C_Milk = df[(df["Sex"]=='F') & (df["Milk type"] == 'C')].count()['Member Name']
F_B_Milk = df[(df["Sex"]=='F') & (df["Milk type"] == 'B')].count()['Member Name']
print 'Females who produce Cow milk ',F_C_Milk,' \nFemales who produce Buffalo milk',F_B_Milk

#Pie Chart for Female producing buffalo and Cow milk
plt.figure()
Labl = ['Cow Milk(Female)','Buffalo Milk(Female)']
b = [F_C_Milk,F_B_Milk]
plt.pie(b,labels = Labl,autopct= make_autopct(b))
plt.legend(Labl,loc = 3)
plt.title('Cow/Buffalo Milk produce by Female Farmer')  #main title for the plot
plt.axis('equal')


#Pie Chart for Male/Female producing buffalo and Cow milk
plt.figure()
Lal = ['Cow Milk(Female)','Buffalo Milk(Female)','Cow Milk(Male)','Buffalo Milk(Male)']
c = [F_C_Milk,F_B_Milk,M_C_Milk,M_B_Milk]
plt.pie(c,labels = Lal,autopct= make_autopct(c))
plt.legend(Lal,loc = 3)
plt.title('Cow/Buffalo Milk produce by Male/Female Farmer')  #main title for the plot
plt.axis('equal')


#male/Females producing Cow/Buffalo Milk Having SNF(Solid Non trans fat) > 9 and SNF < 9
SNF_F_C_Milk_9 = df[(df["Sex"]=='F') & (df["Milk type"] == 'C') & (df['SNF'] >= 8.5 )].count()['SNF']
SNF_F_B_Milk_9 = df[(df["Sex"]=='F') & (df["Milk type"] == 'B') & (df['SNF'] >= 9.0 )].count()['SNF']

SNF_M_C_Milk_9 = df[(df["Sex"]=='M') & (df["Milk type"] == 'C') & (df['SNF'] >= 8.5 )].count()['SNF']
SNF_M_B_Milk_9 = df[(df["Sex"]=='M') & (df["Milk type"] == 'B') & (df['SNF'] >= 9.0 )].count()['SNF']

#Pie Plot For Male And Females Producing Cow/Buffalo Milk with Snf >8.5 for COw and snf > 9 for buffalo
plt.figure()
Array = ['Female Cow Milk SNF>8.5','Female Buffalo Milk SNF>8.5','Male Cow Milk SNF>8.5','Male Buffalo Milk SNF>8.5']
d = [SNF_F_C_Milk_9,SNF_F_B_Milk_9,SNF_M_C_Milk_9,SNF_M_B_Milk_9]
plt.pie(d,labels = Array,autopct= make_autopct(d))
plt.legend(Array,loc = 3)
plt.title('Cow/Buffalo Milk produce by Male/Female Farmer Having SNF greater  8.5')  #main title for the plot
plt.axis('equal')


df['Fat'] = pd.to_numeric(df['Fat'].str.replace(' ',''), errors='force')         #Converting Fat column object to float for summation

  


#Females producing Cow/Buffalo Milk Having Fat Cowmilk => 3 and Buffalo milk >= 5

Fat_F_C_Milk_3 = df[(df["Sex"]=='F') & (df["Milk type"] == 'B') & (df['Fat'] >= 3.0 )].count()['Fat']
Fat_F_B_Milk_5 = df[(df["Sex"]=='F') & (df["Milk type"] == 'B') & (df['Fat'] >= 5.0 )].count()['Fat']

Fat_F_C_Milk_ = df[(df["Sex"]=='F') & (df["Milk type"] == 'C') & (df['Fat'] <= 3.0 )].count()['Fat']
Fat_F_B_Milk_ = df[(df["Sex"]=='F') & (df["Milk type"] == 'B') & (df['Fat'] <= 5.0 )].count()['Fat']


print 'Fat female cow >3 ', Fat_F_C_Milk_3
print 'Fat female cow >5 ', Fat_F_B_Milk_5

#Males producing Cow/Buffalo Milk Having Fat Cowmilk => 3 and Buffalo milk >= 5

Fat_M_C_Milk_3 = df[(df["Sex"]=='M') & (df["Milk type"] == 'C') & (df['Fat'] >= 3.0 )].count()['Fat']
Fat_M_B_Milk_5 = df[(df["Sex"]=='M') & (df["Milk type"] == 'B') & (df['Fat'] >= 5.0 )].count()['Fat']

Fat_M_C_Milk_ = df[(df["Sex"]=='M') & (df["Milk type"] == 'C') & (df['Fat'] <= 3 )].count()['Fat']
Fat_M_B_Milk_ = df[(df["Sex"]=='M') & (df["Milk type"] == 'B') & (df['Fat'] <= 5 )].count()['Fat']

#Pie plot for Fat of Females producing cow/Buffalo milk
plt.figure()
Array = ['Female Cow Milk Fat>3','Female Buffalo Milk Fat>5','Female Cow Milk Fat<3','Female Buffalo Milk Fat<5']
e = [Fat_F_C_Milk_3,Fat_F_B_Milk_5,Fat_F_C_Milk_,Fat_F_B_Milk_]
plt.pie(e,labels = Array,autopct= make_autopct(e))
plt.legend(Array,loc = 2)
plt.title('Cow/Buffalo Milk produce by Female Farmer Having Fat greater or less then 3/5')  #main title for the plot
plt.axis('equal')

#Pie plot for Fat of Males producing cow/Buffalo milk
plt.figure()
Array = ['Male Cow Milk Fat>3','Male Buffalo Milk Fat>5','Male Cow Milk Fat<3','Male Buffalo Milk Fat<5']
f = [Fat_M_C_Milk_3,Fat_M_B_Milk_5,Fat_M_C_Milk_,Fat_M_B_Milk_]
plt.pie(f,labels = Array,autopct= make_autopct(f))
plt.legend(Array,loc = 3)
plt.title('Cow/Buffalo Milk produce by Male Farmer Having Fat greater or less then 3/5')  #main title for the plot
plt.axis('equal')


#Males producing Cow/Buffalo Milk Having Fat Cowmilk => 3 and Buffalo milk >= 5

Fat_C_Milk_3 = df[ (df["Milk type"] == 'C') & (df['Fat'] >= 3.0 )].count()['Fat']
Fat_B_Milk_5 = df[ (df["Milk type"] == 'B') & (df['Fat'] >= 5.0 )].count()['Fat']

Fat_C_Milk_ = df[ (df["Milk type"] == 'C') & (df['Fat'] <= 3 )].count()['Fat']
Fat_B_Milk_ = df[ (df["Milk type"] == 'B') & (df['Fat'] <= 5 )].count()['Fat']

#Pie plot for Fat for all farmers producing cow/Buffalo milk
plt.figure()
Array = ['Cow Milk Fat>3','Buffalo Milk Fat>5','Cow Milk Fat<3','Buffalo Milk Fat<5']
h = [Fat_C_Milk_3,Fat_B_Milk_5,Fat_C_Milk_,Fat_B_Milk_]
plt.pie(h,labels = Array,autopct= make_autopct(h))
plt.legend(Array,loc = 3)
plt.title('Cow/Buffalo Milk produce by Farmers Having Fat greater or less then 3/5')  #main title for the plot
plt.axis('equal')


#Pie plot for Fat for all farmers producing cow/Buffalo milk
plt.figure()
Ary = ['Male Cow Milk Fat>3',' Male Buffalo Milk Fat>5',' Female Cow Milk Fat>3','Female Buffalo Milk Fat>5','Male Cow Milk Fat<3','Male Buffalo Milk Fat<5','Female Cow Milk Fat<3','Female Buffalo Milk Fat<5']
j = [Fat_M_C_Milk_3,Fat_M_B_Milk_5,Fat_F_C_Milk_3,Fat_F_B_Milk_5,Fat_M_C_Milk_,Fat_M_B_Milk_,Fat_F_C_Milk_,Fat_F_B_Milk_]
explode = (0,0,0,0,0.6,0.6,0.6,0.6)
plt.pie(j,labels = Ary,explode = explode,autopct= make_autopct(j))
plt.legend(Ary,loc = 3)
plt.title('Cow/Buffalo Milk produce by Male/Female Farmers Having Fat greater or less then 3/5')  #main title for the plot
plt.axis('equal')




#Top 10 Amount paid to Male Farmer

df['Amount'].reindex()




Top_names = (df.sort_values('Amount',ascending=False).head()[['Qty','Amount','Member Name']])
print Top_names


plt.show()

#////END/////




'''
#Quality vsNnumber of peopl of milk
plt.figure()


plt.ylabel('Number Of Farmers') #y-axis label
plt.xlabel('Fat(%) in Milk')
x = df['Time']
y1 = df['Qty']
y2 = df['Fat']
 
plt.bar(y2,y1,label = x) #creating bar chart
'''

'''
#plt.show()

#print df.dtypes

#print df['Amount'].nlargest(n=5)




plt.figure()
bins = [0,1]
plt.ylabel('Milk produced') #y-axis label
plt.xlabel('Females (Cow/Buffalo)')
id = np.arange(len(b))
width = 0.75
plt.bar(id,b,width,label = Labl) #creating bar chart
plt.xticks(range(4),Labl,rotation = 'vertical',alpha =0.5)  #label for barchart
#plt.xticklabels(Labl,minor = False)
plt.show()
'''




#