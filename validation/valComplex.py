def valComplex (num, array = None):
    status = True
    if not isinstance(num, complex):
        status = False
    
    if array != None:
        complex_num_module = abs(num)

        if isinstance(array, tuple):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered" \
                    "in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than" \
                    "two elements")
            elif complex_num_module <= array[0] or \
                complex_num_module >= array[-1]:
                status = False

        elif isinstance(array, list):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered" \
                    " in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than" \
                    " two elements")
            elif complex_num_module < array[0] or \
                complex_num_module > array[-1]:
                status = False

        else:
            raise TypeError("The second argument is not the right type")
        
    return status  