user_login = "user"
user_pwd = "qwerty"

while True:
    login = str(input("Your login: "))
    pwd = str(input("Your password: "))

    if login == user_login and pwd == user_pwd:
        print("success")
        break
    elif login == 'whatever' or pwd == 'whatever':
        print('access denied')
        break
    else:
        print('try again')