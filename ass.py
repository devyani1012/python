#sumof last four no
num=[1,20,30,40,6,80,70,4,9,60]
sum_last=sum(num[-4:])
print( "sum of  last 4 number:",sum_last)

#difference between max and min
difference=max(num)-min(num)
print ("difference:",difference)

#add no at 6 position 
n=num[3]/3
num.insert(5,n)
print(num)
