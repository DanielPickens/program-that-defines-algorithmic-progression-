def checkIsAP(arr, n): 

    if (n == 1): return True

  

    # Sort array 

    arr.sort() 

  

    # After sorting, difference between 

    # consecutive elements must be same. 

    diffInElem = arr[1] - arr[0] 

    for i in range(2, n): 

        if (arr[i] - arr[i-1] != diffInElem): 

            return False

  

    return True

  
# next 

arr = [180, 30, 180, 80, 130, 130] 

n = len(arr) 

print("Yes") if(checkIsAP(arr, n)) else print("No") 

  
