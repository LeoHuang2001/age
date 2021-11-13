driving = input('請問你是否開過車?')
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你有通過測驗了')
	else:
		print('你無照駕駛')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考駕照喔')
	else:
 		print('之後就可以考了')
else:
	print('請輸入有或沒有')