x=int(input())
y=int(input())
z=int(input())
result=int(input())
count=0
for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                    if (i*500+j*100+k*50)==result:
                        count+=1
                        print(i,j,k)
print(count)
