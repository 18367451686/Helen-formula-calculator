import os
print("三角形三边长求面积")
print("设abc是三角形三边边长")
print("开发者信息：\n鼎天网络\nDTNETWORK\nGary Chan")
print("感谢使用")
print("注意，由于算法问题，abc需大于1")
import math

a1 = input("a=")
b1 = input("b=")
c1 = input("c=")


a4 = int(a1)
b4 = int(b1)
c4 = int(c1)

l = ( a4 + b4 + c4 )
p = ( l ) / 2

p2 = int(p)

s = ( p2 * ( p2 - a4 ) * ( p2 - b4 ) * ( p2 - c4 ) ) ** ( 1 / 2 )

s2 = str(s)

l2 = str(l)

print("周长（l）=" + l2 )

print("面积（s）=" + s2 )
e = "单击任意键退出"
print(e)
os.system("pause")