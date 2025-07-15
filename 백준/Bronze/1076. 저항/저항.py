color = {'black':1,'brown':10,'red':100,'orange':1000,'yellow':10000,'green':100000,'blue':1000000,'violet':10000000,'grey':100000000,'white':1000000000}
color_list=list(color.keys())

a1=input()
a2=input()
a3=input()

c1=color_list.index(a1)
c2=color_list.index(a2)
c3=color[a3]

print(int(str(c1)+str(c2))*c3)