#ans = input('請你輸入溫度:')

while True:
	print('歡迎使用本公司服務。')
	ans = input('請你輸入現時溫度:')
	#print(ans[1:])
	if ans[0] == 'q':
		break
	elif ans[0] == 'F':
		c = int(ans[1:])/9*5+32
		#print(f)
		print('現在的溫度為', 'C', round(c, 1), '度')
	elif ans[0] == 'C':
		#print(c)
		f = int(ans[1:])/9*5+32
		print('現在的溫度為'+'F', round(f, 1), '度')
	else:
		print('請輸入華氏／攝氏溫度')

print('多謝便用本服務')