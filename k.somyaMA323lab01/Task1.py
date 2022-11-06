A=[3,6]
b=0
m=11
for a in A:
  print('For a=%d'%a + ' , b=0, m=11')
  for x in range(11):
    xi=x
    L=[]
    print('Xo = %d'%xi)
    L.insert(len(L),xi)
    for t in range(20):
      xi=(a*xi+b)%m
      L.insert(len(L),xi)
    print(L)
  print("\n")
