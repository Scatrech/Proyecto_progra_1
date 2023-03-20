#menu   Brandon Ramírez
print('Seleccione el tipo de conversion que desea realizar')
print('1 - Conversor de Longitud')
print('2 - Conversor de Peso')
print('3 - Conversor de Bytes')
print('4 - Conversor de base numérica')
opcion_menu = int(input('Ingrese un numero para escoger: '))


#longitud
if opcion_menu == 1:
    # Pedimos al usuario la longitud y la unidad de longitud de entrada
    longitud = float(input("Ingrese la longitud: "))
    unidad_entrada = input("Ingrese la unidad de longitud de entrada (cm/m/km): ")

  #Convertir a cm
    if unidad_entrada == "cm":
        longitud_en_cm = longitud
    elif unidad_entrada == "m":
        longitud_en_cm = longitud * 100
    elif unidad_entrada == "km":
        longitud_en_cm = longitud * 100000
    else:
        print("Unidad de longitud de entrada no válida")
        exit()

    # Pedimos al usuario la unidad de longitud de salida
    unidad_salida = input("Ingrese la unidad de longitud de salida (cm/m/km): ")

    # Convertimos la longitud de centímetros a la unidad de salida especificada
    if unidad_salida == "cm":
        longitud_convertida = longitud_en_cm
    elif unidad_salida == "m":
        longitud_convertida = longitud_en_cm / 100
    elif unidad_salida == "km":
        longitud_convertida = longitud_en_cm / 100000
    else:
        print("Unidad de longitud de salida no válida")
        exit()

    # Longitud final
    print("La longitud convertida es:", longitud_convertida, unidad_salida)

#Peso

if opcion_menu == 2:
    # Pedimos al usuario el peso y la unidad de peso de entrada
    peso = float(input("Ingrese el peso: "))
    unidad_entrada = input("Ingrese la unidad de peso de entrada (onz, lb, kg): ")

    # Convertimos el peso a onz
    if unidad_entrada == 'onz':
        longitud_en_onz = peso
    elif unidad_entrada == 'lb':
        longitud_en_onz  = peso * 16
    elif unidad_entrada == 'kg':
        longitud_en_onz = peso * 35.274
    else:
        print("Unidad de peso de entrada no válida")
        exit()

    # Pedimos al usuario la unidad de peso de salida
    unidad_salida = input("Ingrese la unidad de peso de salida (onz, lb, kg): ")

    # Convertir a onz
    if unidad_salida == "onz":
        peso_convertida = longitud_en_onz
    elif unidad_salida == "lb":
        peso_convertida = longitud_en_onz / 16
    elif unidad_salida == "kg":
        peso_convertida = longitud_en_onz / 35.274
    else:
        print("Unidad de peso de salida no válida")
        exit()
# Peso final
    print("El peso convertido es de:", peso_convertida, unidad_salida)
    exit()

#bytes

if opcion_menu == 3:
    # Pedimos al usuario los bytes y la unidad de bytes de entrada
    byte = float(input("Ingrese los bytes a convertir: "))
    unidad_entrada = input("Ingrese la unidad de bytes de entrada (B, KB, MB): ")

    # Convertimos el peso a bytes
    if unidad_entrada == 'B':
        peso_en_bytes = byte
    elif unidad_entrada == 'KB':
        peso_en_bytes = byte * 1000
    elif unidad_entrada == 'MB':
        peso_en_bytes = byte * 1000000
    else:
        print("Unidad de bytes de entrada no válida")
        exit()

    # Pedimos al usuario la unidad de peso de salida
    unidad_salida = input("ingrese la unidad de bytes"
                          ""
                          ""
                          " de salida (B, KB, MB): ")

    # Convertir a bytes
    if unidad_salida == "B":
        bytes_convertidos = peso_en_bytes
    elif unidad_salida == "KB":
        bytes_convertidos = peso_en_bytes / 1000
    elif unidad_salida == "MB":
        bytes_convertidos = peso_en_bytes / 1000000
    else:
        print("Unidad de salida no válida")
        exit()
# Peso final
    print("El peso convertido es de:", bytes_convertidos, unidad_salida)
    exit()

#base

if opcion_menu == 4:
    # Pedimos al usuario el número decimal a convertir
    numero_decimal = int(input("Ingrese un número decimal: "))

    # Pedimos al usuario la base a la que se quiere convertir el número decimal
    print("Seleccione la base a la que desea convertir el número decimal:")
    print("1. Binario")
    print("2. Octal")
    print("3. Decumal")
    opcion = int(input("Ingrese una opción: "))

    numero_convertido = ""

    # Convertimos el número decimal a la base elegida por el usuario
    if opcion == 1:
        while numero_decimal > 0:

            residuo = numero_decimal % 2
            numero_convertido = str(residuo) + numero_convertido
            numero_decimal = numero_decimal // 2

    elif opcion == 2:
        # Convertimos el número decimal a octal
        while numero_decimal > 0:
            residuo = numero_decimal % 8
            numero_convertido = str(residuo) + numero_convertido
            numero_decimal = numero_decimal // 8

    elif opcion == 3:
        numero_convertido = numero_decimal

    else:
        # Si el usuario ingresó una opción inválida, mostramos un mensaje de error
        print("Opción inválida")
        exit()

    # Mostramos el número convertido al usuario
    if opcion == 1:
        print("El número en binario es:", numero_convertido)
    elif opcion == 2:
        print("El número en octal es:", numero_convertido)
    elif opcion == 3:
        print("El número en decimal:", numero_convertido)


print('Gracias, Brandon Ramírez')





