country = input('請問你是哪一個國家的人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18 :
		print ('可以開車')
	else :
		print('你不能考駕照')
else :
	print('你不是台灣人,只能問你自己的國家!')