# you will be given n and k  
# find the nth fibonacci number which is a multiple of k  
# return its position

def fibonacci(n,k):
  position = 0
  n1 = 0
  n2 = 1
  if(n2%k == 0):
    n -= 1
  position += 1
  
  while(n > 0):
    num = n1 + n2
    if(num % k == 0):
      n -= 1
    n1 = n2
    n2 = num
    position += 1
  return position



n,k = input().split(" ")
n = int(n)
k = int(k)
print(fibonacci(n,k))
