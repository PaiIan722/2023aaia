a = [9,8,7,6,5,4,3,2,1,0]
N = len(a)
print(a)
for k in range(N): #很多次
  for i in range(N-1): #一輪的泡泡
    if a[i] > a[i+1]:
      a[i], a[i+1] = a[i+1], a[i]
  print(a)