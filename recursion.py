def collatz(n):
    list1 = [n]
    if n == 1 :
        return [1]                 
    elif n % 2 == 0 :
         
        list1.extend(collatz(n//2))     
    else:
        list1.extend(collatz(n*3+1))    
    return list1
 
collatz(128)
