def prime(num):
    flag=False
    for a in range(2,num-1): #basically prime no are divisible by itself and by 1 only so set input value -1 so i takes previous num
        if num%a==0:
            flag=True
    if flag==False:
        print("prime")
    else:
        print("not prime")


num=int(input("enter the no"))
prime(num)

