alphabet=input("enter alphabet")
num=int(input("enter num"))
spl_cha=input("enter spl_cha")
a="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"or"A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
b=1,2,3,4,5,6,7,8,9
c="@,#,$,%,&"
if alphabet in (a):
    print("your password enter alphabet=a") 
elif num in (b):
    print("your password enter num=b")
elif spl_cha in "c":
    print("your password enter spl_cha=c")
    num=str(num) 
    sum=alphabet+num+spl_cha
    print(sum,"your password is strong")
else:
    print("your password not")           