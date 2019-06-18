country = input('請問你是哪一個國家的人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18 :
		print ('可以開車')
	else :
		print('你不能考駕照')
elif country == '美國' :
	if age >=16 :
		print ('老美你好,你可以考駕照!')
	else :
		print('你沒資格考駕照')
else:
	print('你不是老美也不是彎彎,只能問你的國家能不能考駕照')