print("Hello Word")
# assign (gán) 1 cho biến a cả đống đó đc gọi là 1 assignment statement( mệnh đề gán giá trị)
a= 1

print("a =" + str(a))

print("-----------------------------------------------")
print("Nhap số USD")
usd = input()
vnd = int(usd) * 22

print(str(usd)+ "USD ="+str(vnd)+"k VND")
print("-----------------------------------------------")
x=1 
y=2
print("x= "+str(x))
print("y = "+str(y))
temp =x;
x=y
y= temp
print("----")
print("x= "+str(x))
print("y = "+str(y))
print("-----------------------------------------------")
age =input()
numberAge=int(age)
if numberAge < 10:
	print("Tre em ")
elif numberAge < 18:
	print("Vi thanh nien")
	if numberAge >11 and numberAge <17:
		print("Tre trau")
else:
	print("Nguoi lon")
