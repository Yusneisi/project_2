def valList (array, var = None, string = None):
    status = True
    if not isinstance(array, list):
        status = False
    
    if var != None or string != None:
        if string == "value":
            if isinstance(var, list):
                if not var == array:
                    status = False 
            else:
                status = False 
        elif string == "len":
            if isinstance(var, int):
                var = str(var)
                if not len(array) == len(var):
                    status = False 
            else:
                status = False
        else:
            if var != list or var != int:
                raise TypeError("The second argument is not "
                    "of a list or int type")
            else:
                raise ValueError("The third argument is not 'value' "
                    "or 'len'")

    return status
