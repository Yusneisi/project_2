def valFloat (num, array = None):
    variable = True
    if not isinstance(num, float):
        variable = False
    
    if array != None:
        if isinstance(array, tuple):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered" \
                    "in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than" \
                    "two elements")
            elif num <= array[0] or num >= array[-1]:
                variable = False
        elif isinstance(array, list):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered" \
                    " in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than" \
                    " two elements")
            elif num < array[0] or num > array[-1]:
                variable = False
        else:
            raise TypeError("The second argument is not the right type")

    return variable