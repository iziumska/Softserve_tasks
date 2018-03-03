def natural_number(max_number):
    list = []
    for number in range(1, (max_number+1)):
        if number * number < max_number:
            list.append(number)
    return list
