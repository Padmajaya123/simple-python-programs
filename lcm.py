n1=int(input())
n2=int(input())
if(n1>n2 ):
    max=n1
else:
    max=n2
while(True):
    if(max%n1==0 and max%n2==0):
        print("LCM=",max)
        break;
    max= max+1