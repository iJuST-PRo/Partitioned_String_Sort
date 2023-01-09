
def partitioned_string_sort(text):
    filtered_text = ''.join(filter(str.isalnum, text))

    previous_character = filtered_text[0]
    newword = filtered_text[0]
    splitted = []

    for x, i in enumerate(filtered_text[1:]):
        if i.isalpha() and previous_character.isalpha():
            newword += i
        elif i.isnumeric() and previous_character.isnumeric():
            newword += i
        else:
            splitted.append(newword)
            newword = i

        previous_character = i

        if x == len(filtered_text) - 2:
            splitted.append(newword)
            newword = ''

    ready = [''.join(sorted(string)) for string in splitted]
    final = ''.join(ready)

    return print(final)


if __name__=='__main__':
    text = input('Enter the string: ')
    partitioned_string_sort(text)