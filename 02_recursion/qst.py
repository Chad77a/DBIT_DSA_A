def new_func(n):
<<<<<<< HEAD
    #new_func(n)
    if n==0:
        #print("Stop")
        return 0
    else:
        print(f"Value of n is {n}")
        
=======
    # new_func(n)
    if n == 0:
        # print("Stop")
        return 0
    else:
        print(f"Value of n is {n}")
        new_func(n - 1)  # function calling itself 
    
new_func(5)
>>>>>>> 63aaf2723f14d837f3a78af85139f104e8f2acc1
