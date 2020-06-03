country = input('你所在的國家: ')
age = input('你的年齡: ')
age = int(age)
if country == '美國' and age >= 16:
	print('你可以開車')
elif country == '台灣' and age >= 18:
	print('你可以開車')
else:
	print('你不能開車')

