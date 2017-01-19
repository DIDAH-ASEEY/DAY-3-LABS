def find_missing(x,y):

    if len(x)==len(y):
        return 0
    else:
        for num in x:
            if num not in y:
                return num
        else:
            for num in y:
                if num not in x:
                    return num

                

    


        
            
            
