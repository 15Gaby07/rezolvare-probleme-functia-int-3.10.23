#problema12
a=int(input('Gaina 1= '))
b=int(input('Gaina 2= '))
c=int(input('Gaina 3= '))
d=int(input('Gaina 4= '))
print('totul est egal',7*(a+b+c))

#problema11
a=int(input('Iepuri la inceputul lunii= '))
b=int(input('Iepuri morti= '))
c=int(input('Iepuri nascuti= '))
print('La sfarsitul lunii au ramas', a+b+c, 'iepuri')

#problema10
n=int(input('n= '))
print(n,'*',1,'=', n*1)
print(n,'*',2,'=', n*2)
print(n,'*',3,'=', n*3)
print(n,'*',4,'=', n*4)
print(n,'*',5,'=', n*5)
print(n,'*',6,'=', n*6)
print(n,'*',7,'=', n*7)
print(n,'*',8,'=', n*8)
print(n,'*',9,'=', n*9)
print(n,'*',10,'=', n*10)


#problema 9
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
print(a,'+',b,'=', a+b)
print(a,'+',b,'=', a+c)
print(b,'+',c,'=', b+c)

#problema8
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
print(a*100+b*10+c,'',a*100+c*10+b,'',b*100+c*10+a,'',b*100+a*10+c,'',c*100+a*10+b)

#problema7
#varsta
v=int(input('introdu varsta: '))
greutate=2*v+8
inaltime=5*v+8
print('pentru varsta de',v,'ani', 'greutatea ideala este de: ',greutate,'kg','iar inaltimea ideala este de:', inaltime, 'cm')

#problema6
m=int(input('m= '))
n=m
print('Copil 1= ', m-2, 'mere')
print('Copil 2= ', n+1, 'mere')

# problema 1
n=int(input("Dati numarul de rand al culorii curcubeului"))
if n==1:
    print("rosu ")
if n==2:
    print('oranj ')  
if n==3:
    print('galben ')
if n==4:
    print('verde')  
if n==5:
    print('albastru')      
if n==6:
    print('indigo')   
if n==7:
    print('violet')        

# problema 3
n1=int(input('statie 1= '))
n2=int(input('statie 2= '))
print('numarul total de elevi in autobuz este: ', n1+n2+7)

#problema 4
a=int(input('Dati numarul de globulete albe '))  
r=a+3
ab=(a+r)-2
print('Numarul total de globulete= ', a+r+ab)
