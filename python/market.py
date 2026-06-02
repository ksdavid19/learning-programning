import os
client_ident = []
client_name = []
client_address = []
client_phone = []
client_email = []
client_gender = []
client_age = []
product_code = []
product_name = []
product_quantity = []
product_value = []

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("1. Registrar cliente")
    print("2. Registrar producto")
    print("3. Listar clientes")
    print("4. Listar productos")
    print("5. Buscar cliente")
    print("6. Buscar producto")
    print("7. Actualizar cliente")
    print("8. Actualizar producto")
    print("9. Eliminar cliente")
    print("10. Eliminar producto")
    print("11. Salir")

    try:
        opt = int(input("Opción: "))
    except ValueError:
        print("Ingrese un número válido")
        input("Presione Enter para continuar...")
        continue


    if opt == 1:

        ident = input("Identificación: ")

        if ident in client_ident:
            print("La identificación ya existe")
        else:
            client_ident.append(ident)
            client_name.append(input("Nombre completo: "))
            client_address.append(input("Dirección: "))
            client_phone.append(input("Teléfono: "))
            client_email.append(input("Correo electrónico: "))
            client_gender.append(input("Género: "))
            client_age.append(int(input("Edad: ")))

            print("Cliente registrado")

        input("Presione Enter para continuar...")

   
    elif opt == 2:

        code = input("Código del producto: ")

        if code in product_code:
            print("El código ya existe")
        else:
            product_code.append(code)
            product_name.append(input("Nombre del producto: "))
            product_quantity.append(int(input("Cantidad: ")))
            product_value.append(float(input("Valor unitario: ")))

            print("Producto registrado")

        input("Presione Enter para continuar...")


    elif opt == 3:

        if len(client_ident) == 0:
            print("No hay clientes registrados")
        else:
            for i in range(len(client_ident)):
                print("\n--------------------")
                print("Identificación:", client_ident[i])
                print("Nombre:", client_name[i])
                print("Dirección:", client_address[i])
                print("Teléfono:", client_phone[i])
                print("Correo:", client_email[i])
                print("Género:", client_gender[i])
                print("Edad:", client_age[i])

        input("\nPresione Enter para continuar...")


    elif opt == 4:

        if len(product_code) == 0:
            print("No hay productos registrados")
        else:
            for i in range(len(product_code)):
                print("\n--------------------")
                print("Código:", product_code[i])
                print("Nombre:", product_name[i])
                print("Cantidad:", product_quantity[i])
                print("Valor unitario:", product_value[i])

        input("\nPresione Enter para continuar...")


    elif opt == 5:

        ident = input("Identificación: ")

        if ident in client_ident:
            pos = client_ident.index(ident)

            print("\nCliente encontrado")
            print("Nombre:", client_name[pos])
            print("Dirección:", client_address[pos])
            print("Teléfono:", client_phone[pos])
            print("Correo:", client_email[pos])
            print("Género:", client_gender[pos])
            print("Edad:", client_age[pos])
        else:
            print("Cliente no encontrado")

        input("\nPresione Enter para continuar...")

 
    elif opt == 6:

        code = input("Código del producto: ")

        if code in product_code:
            pos = product_code.index(code)

            print("\nProducto encontrado")
            print("Nombre:", product_name[pos])
            print("Cantidad:", product_quantity[pos])
            print("Valor unitario:", product_value[pos])
        else:
            print("Producto no encontrado")

        input("\nPresione Enter para continuar...")

   
    elif opt == 7:

        ident = input("Identificación: ")

        if ident in client_ident:
            pos = client_ident.index(ident)

            client_name[pos] = input("Nuevo nombre: ")
            client_address[pos] = input("Nueva dirección: ")
            client_phone[pos] = input("Nuevo teléfono: ")
            client_email[pos] = input("Nuevo correo: ")
            client_gender[pos] = input("Nuevo género: ")
            client_age[pos] = int(input("Nueva edad: "))

            print("Cliente actualizado")
        else:
            print("Cliente no encontrado")

        input("\nPresione Enter para continuar...")

   
    elif opt == 8:

        code = input("Código del producto: ")

        if code in product_code:
            pos = product_code.index(code)

            product_name[pos] = input("Nuevo nombre: ")
            product_quantity[pos] = int(input("Nueva cantidad: "))
            product_value[pos] = float(input("Nuevo valor unitario: "))

            print("Producto actualizado")
        else:
            print("Producto no encontrado")

        input("\nPresione Enter para continuar...")

  
    elif opt == 9:

        ident = input("Identificación: ")

        if ident in client_ident:
            pos = client_ident.index(ident)

            del client_ident[pos]
            del client_name[pos]
            del client_address[pos]
            del client_phone[pos]
            del client_email[pos]
            del client_gender[pos]
            del client_age[pos]

            print("Cliente eliminado")
        else:
            print("Cliente no encontrado")

        input("\nPresione Enter para continuar...")

    elif opt == 10:

        code = input("Código del producto: ")

        if code in product_code:
            pos = product_code.index(code)

            del product_code[pos]
            del product_name[pos]
            del product_quantity[pos]
            del product_value[pos]

            print("Producto eliminado")
        else:
            print("Producto no encontrado")

        input("\nPresione Enter para continuar...")

    # SALIR
    elif opt == 11:
        print("Hasta luego")
        break

    else:
        print("Opción inválida")
        input("Presione Enter para continuar...")
