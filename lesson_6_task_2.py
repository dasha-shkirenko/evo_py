def find_letter(txt):
    # message = ''
    #
    # for i in range(len(txt)):
    #     if txt[i].isupper():
    #         message += txt[i]

    message = ''.join([txt[i] for i in range(len(txt)) if txt[i].isupper()])

    return message


a = 'Hello WorldRT kOggkgghghYYYYYYY'

print(find_letter(a))