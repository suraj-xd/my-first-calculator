end =True
def cal(a, b):
    if(c=='+'):
        print(a + b)
    if(c=='-'):
        print(a - b)
    if(c=='*'):
        print(a * b)
    if(c=='/'):    
        print(a / b)
while (end):
        a = int(input())
        c = str(input())
        b = int(input())
        print("=")
        cal(a, b)
        d = str(input("~ENTER 'Q' to QUIT - \n~ENTER 'C' TO CONTINUE- \n"))
        if (d == 'q' or d=='Q'):
            end = False
        elif(d == 'c' or d == 'C'):
            end = True
