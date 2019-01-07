Cookies=[[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]]

def Classic_cookies(myCookie):
    print('This is my cookie')
    for i in myCookie:
        print(i)
    k=0
    count=0
    result=[]
    while k<=4:
        for chips in myCookie:
            if chips[k]==1:
                count+=1
            if chips[k]==0:
                res=count
                if res==0:
                    pass
                else:
                    result.append(res)
                count=0
        k+=1
    return result
print(f"This is the result of your challenge {Classic_cookies(Cookies)}")
