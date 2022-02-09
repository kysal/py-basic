import basic

print("Hello World")
while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
