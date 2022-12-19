def replace_none(lst):
    # Initialize the new list and the current value
    new_list = []
    current_value = None

    # Iterate over the original list
    for value in lst:
        if value is not None:
            # If the value is not None, update the current value
            current_value = value
        else:
            # If the value is None, use the current value
            value = current_value
        # Append the value (either the original or the current value) to the new list
        new_list.append(value)

    return new_list

# Test the function
lst = [3,None,2,None,None,1,False,None,10]
print(replace_none(lst))  # Output: [3,3,2,2,2,1,False,False,10]
