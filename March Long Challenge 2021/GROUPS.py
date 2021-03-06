# cook your dish here
for _ in range(int(input())):
    s=input()
    c=0
    if len(s)==1 and s[0]=='1':
        c+=1
        
    for i in range(1,len(s)):
        if s[i-1]=='0' and s[i]=='1':
            c+=1
        if s[i-1]=='0' and s[i]=='0':
            pass
        if(s[i-1]=='1' and s[i]=='1') and i==1:
            c+=1
        if s[i-1]=='1' and s[i]=='1':
            pass
        if(s[i-1]=='1' and s[i]=='0') and i==1:
            c+=1
    print(c)
            
            
        
