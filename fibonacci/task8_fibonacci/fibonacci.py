def creating_user_fibonacci_list(start, end):
    fibonacci_list = [1, ]

    for i in range(1, end+1):
        if i == 1 or i == 2:
            fibonacci_list.append(i)
        elif i == 3:
            fibonacci_list.append(i)
        else:
            b = fibonacci_list[i-1] + fibonacci_list[i-2]
            fibonacci_list.append(b)
    user_list = []
    for b in fibonacci_list:
        if start <= b <= end:
            user_list.append(b)
    return user_list


def print_out_user_list(start, end, user_list):
    print('From the number {} to the number {}, the Fibonacci '
          'numbers are: {}'.format(start, end, user_list))
