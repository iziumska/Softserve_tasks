# !/usr/bin/env python


def counting_string(file_name, sourse_text):
    with open(file_name, 'r') as file:
        data = file.read()
        words = data.count(sourse_text)
        print('{} lines in the file {}'.format(words, file_name))
        return words


def replace_string(file_name, sourse_text, replace_text):
    with open(file_name, 'r') as file:
        old_data = file.read()
        if sourse_text in old_data:
            new_data = old_data.replace(sourse_text, replace_text)
            with open(file_name, 'w') as file2:
                file2.write(new_data)
                print('It turned out to replace {} with {}'.
                      format(sourse_text, replace_text))
        else:
            print('The string to replace is not entered correctly')
        return replace_text
