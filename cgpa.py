file=open('a.txt','r')
a=file.read()
num=a.split('\\n\\')
for i in range(len(num)):
    num[i]=num[i][1:]
l=[]
for i in range(len(num)):
    if num[i]=='SGPA':
        l.append(num[i+1])
print("sgpa is : ",l)
temp=[]
for i in range(len(num)):
    if num[i][0]==' ':
        temp.append(num[i])
credit=[]
var=[]
for i in temp:
    if i[1:].isdigit():
        var.append(i[1:])
    else:
        if len(var):
            credit.append(var)
        var=[]
grade=[]
temp=[]
comp=['S','A','B','C','D','E','P']
for i in range(len(num)):
    if num[i] in comp:
        temp.append(num[i])
    else:
        if len(temp)<=6:
            continue
        else:
            grade.append(temp)
            temp=[]
a={'S':10,'A':9,'B':8,'C':7,'D':6,'E':5,'F':4,'P':0}
new=[]
for i in range(len(grade)):
    val=0
    credits=0
    for j in range(len(grade[i])):
        val+=int(credit[i][j])*a[grade[i][j]]
        credits+=int(credit[i][j])
    new.append([val,credits])
for i in range(len(grade)):
    count=0
    for j in range(len(grade[i])):
        if grade[i][j]=='P':
            new[i][1]-=int(credit[i][j])
            print(grade[i][j],i,j,count,new[i][1])

sgpa=[]
for i in new:
    sgpa.append(i[0]/i[1])
print("sgpa : ",sgpa)
tot=0
den=0
for i in new:
    tot+=i[0]
    den+=i[1]
print('cgpa is : ',tot/den)