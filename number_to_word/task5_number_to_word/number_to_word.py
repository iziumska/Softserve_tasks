def number_to_word(n):
    list_to_twenty = ['ноль', 'один', 'два', 'три', 'четыре',
                      'пять', 'шесть', 'семь', 'восемь',
                      'девять', 'десять', 'одиннадцать',
                      'двенадцать', 'тринадцать',
                      'четырнадцать', 'пятнадцать',
                      'шестнадцать', 'семнадцать',
                      'восемнадцать', 'девятнадцать']
    list_to_one_hundred = [' ', ' ', 'двадцать', 'тридцать',
                           'сорок', 'пятьдесят', 'шестьдесят',
                           'семьдесят', 'восемьдесят', 'девяносто']
    list_to_thousand = [' ', 'сто', 'двести', 'триста', 'четыреста',
                        'пятьсот', 'шестьсот', 'семьсот', 'восемьсот',
                        'девятьсот']

    value = 'минус ' if n < 0 else ''

    if n <= 0 or n > 0:
        if n < 0:
            n = abs(n)
            # minus = 'минус '
            # print('минус ', end='')
        if n >= 0:
            if n == 0 or n < 20:
                word = (list_to_twenty[n])
            elif n == 20 or n < 100:
                if n % 10 == 0:
                    s = int(n / 10)
                    word = (list_to_one_hundred[s])
                elif n % 10 != 0:
                    c = n % 10
                    m = int((n - c) / 10)
                    word = (list_to_one_hundred[m] + ' ' + list_to_twenty[c])
            elif n == 100 or n < 1000:
                if n % 100 == 0:
                    h = int(n / 100)
                    word = (list_to_thousand[h])
                elif n % 100 != 0:
                    d = n % 100
                    h = int((n - d) / 100)
                    if d < 20:
                        word = (list_to_thousand[h] + ' ' + list_to_twenty[d])
                    elif d == 20 or d < 100:
                        if d % 10 == 0:
                            s = int(d / 10)
                            word = (list_to_thousand[h] +
                                    ' ' + list_to_one_hundred[s])
                        elif d % 10 != 0:
                            c = d % 10
                            m = int((d - c) / 10)
                            word = (list_to_thousand[h] +
                                    ' ' + list_to_one_hundred[m] +
                                    ' ' + list_to_twenty[c])

    return value + word
