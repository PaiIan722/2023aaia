a = 1500000000 #把數字變很大,變成15億 老大
b = 2000000000 #把數字變很大,變成20億 老二

c = a%b #老三
print(a, b, c)
while c!=0: #輾轉相除法
  a = b #老二升格變老大
  b = c #老三升格變老二
  c = a%b #新的老三算出來
  print(a, b, c)
print(b)