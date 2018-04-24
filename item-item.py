
import csv
from decimal import Decimal
import math
def maxm(a, b):
    if a>=b:
        return a
    return b

#similarity value between two item vectors
def sim(item1, item2):
    userCount=len(item1)
    # print item1, item2
    sum1=0
    sum2=0
    for i in range(userCount):
        sum1=sum1+item1[i]
        sum2=sum2+item2[i]
    avg1=Decimal(Decimal(sum1)/Decimal(userCount))
    avg2=Decimal(Decimal(sum2)/Decimal(userCount))
    # print sum1, sum2, avg1, avg2
    for i in range(userCount):
        if(item1[i]!=0):
            item1[i]=Decimal(item1[i]-avg1)
        if(item2[i]!=0):
            item2[i]=Decimal(item2[i]-avg2)
    psum=0
    prod1=0
    prod2=0
    for i in range(userCount):
        psum=psum+Decimal(item1[i]*item2[i])
        prod1=(prod1+(item1[i]**2))
        prod2=(prod2+(item2[i]**2))
    prod1=math.sqrt(prod1)
    prod2=math.sqrt(prod2)

    fprod=Decimal(prod1*prod2)

    return Decimal(psum/fprod)

fname="utility.txt"
dataset=[]
itemCount=0
userCount=0

with open(fname) as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        line = map(int, line)
        line = list(line)
        # print line
        dataset.append(line)


# print dataset

for i in range(len(dataset)-1):
    itemCount=maxm(itemCount, dataset[i][1])
    userCount=maxm(userCount, dataset[i][0])

utilityMatrix=[]

print "No of users, ", userCount
print "No of items, ", itemCount

for i in range(itemCount+1):
    array=[]
    for j in range(userCount+1):
        array.append(0)
    utilityMatrix.append(array)
print len(dataset)

for i in range(len(dataset)-1):
    utilityMatrix[dataset[i][1]][dataset[i][0]]=dataset[i][2]

for i in range(1, 11):
    for j in range(1, 11):
        print utilityMatrix[i][j],
    print "\n"

for i in range(1, itemCount):
    print sim(utilityMatrix[1], utilityMatrix[i])
