#1 upper 메서드 
#ticker = "btc_krw"
#print(ticker.upper())

#2 lower 메서드
#ticker = "BTC_KRW"
#print(ticker.lower())

#3 capitalize 메서드
#str = "hello"
#print(str.capitalize())

#4 endswitch 메서드 
#file_name = "보고서.xlsx"
#file_name.endswith(("xlsx","xls"))

#7 공백을 기준으로 문자열 나누기
a = "hello world"
b = a[:a.find(" ")]
c = a[a.find(" "):]

print(b,"\n",c)