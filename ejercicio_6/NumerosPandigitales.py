def NumerosPandigitales():
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num = input()
    panDig = True
    dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
            '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

    for i in numeros:
        if i not in num:
            panDig = False
        else:
            dict[i] = dict[i] + 1
    if panDig and num[0] != 0:
        print("el número" + num + "es pandigital")
    else:
        print("el número" + num + "no es pandigital")
