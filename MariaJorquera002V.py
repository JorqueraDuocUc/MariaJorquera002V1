def validar_entero_positivo(valor):
    try:
        valor_entero = int(valor)
        return valor_entero > 0
    except ValueError:
        return False

def validar_entero_no_negativo(valor):
    try:
        valor_entero = int(valor)
        return valor_entero >= 0
    except ValueError:
        return False

def validar_peso(valor):
    try:
        valor_flotante = float(valor)
        return valor_flotante > 0
    except ValueError:
        return False

def validar_texto(texto):
    return texto.strip() != ""

def validar_si_no(valor):
    valor = valor.strip().lower()
    return valor == "s" or valor == "n"

def convertir_si_no_a_booleano(valor):
    valor = valor.strip().lower()
    return valor == "s"

def buscar_codigo(productos, codigo):
        return codigo.strip().upper() in productos

def validar_codigo(productos, codigo):
    codigo_limpio = codigo.strip().upper()
    if codigo_limpio == "":
        return False
    if buscar_codigo(productos, codigo_limpio):
        return False
    return True

def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1.- Unidades por categoria")
    print("2.- Busqueda de productos por rango de precio")
    print("3.- Actualizar precio de producto")
    print("4.- Agregar producto")
    print("5.- Eliminar producto")
    print("6.- Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida (1-6)")
        except ValueError:
            print("Debe seleccionar una opción válida")

def unidades_categoria(productos, stock, categoria):
    categoria = categoria.strip().lower()
    total_unidades = 0
    for codigo, info in productos.items():
        categoria_producto = info[1]
        if categoria_producto.lower() == categoria:
            total_unidades += stock[codigo][1]
    print(f"El total de unidades disponibles es: {total_unidades}")

def pedir_rango_precio():
    while True:
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
        except ValueError:
            print("Debe ingresar valores enteros")
            continue
        
        if p_min < 0 or p_max < 0:
            print("Los precios deben ser mayores o iguales a cero.")
        elif p_min > p_max:
            print("El precio mínimo no puede ser mayor que el precio máximo.")
        else:
            return p_min, p_max

def busqueda_precio(productos, stock, p_min, p_max):
    encontrados = []
    for codigo, info_stock in stock.items():
        precio = info_stock[0]
        unidades = info_stock[1]
        if p_min <= precio <= p_max and unidades != 0:
            nombre = productos[codigo][0]
            encontrados.append(f"{nombre}--{codigo}")
    
    encontrados.sort()
    if not encontrados:
        print("No hay productos en ese rango de precios.")
    else:
        print(f"Los productos encontrados son: {encontrados}")

def actualizar_precio(productos, stock, codigo, nuevo_precio):
    codigo = codigo.strip().upper()
    if codigo in stock:
        stock[codigo][0] = nuevo_precio
        return True
    return False

def agregar_producto(productos, stock, codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    codigo = codigo.strip().upper()
    if codigo in productos:
        return False
    productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
    stock[codigo] = [precio, unidades]
    return True

def eliminar_producto(productos, stock, codigo):
    codigo = codigo.strip().upper()
    if codigo in productos:
        del productos[codigo]
        del stock[codigo]
        return True
    return False

def main():
    productos = {
        "M001": ["Alimento Premium", "comida", "DogPlus", 10, True, False],
        "M002": ["Arena Aglomerante", "higiene", "CatClean", 8, False, False],
        "M003": ["Snack Dental", "snack", "BiteJoy", 1, True, True],
        "M004": ["Shampoo Suave", "higiene", "PetCare", 0.5, False, True],
        "M005": ["Correa Nylon", "accesorio", "WalkPro", 0.3, True, False],
        "M006": ["Cama Mediana", "accesorio", "CozyPet", 2, False, False],
        }
    stock = {
         "M001": [32990, 12],
        "M002": [9990, 0],
        "M003": [5490, 25],
        "M004": [7990, 5],
        "M005": [11990, 7],
        "M006": [24990, 3],
    }

    while True:
        mostrar_menu()
        opcion = leer_opcion()
        match opcion:
            case 1:
                categoria = input("Ingrese categoría a consultar: ")
                unidades_categoria(productos, stock, categoria)
            case 2:
                p_min, p_max = pedir_rango_precio()
                busqueda_precio(productos, stock, p_min, p_max)
            case 3:
                continuar = "s"
                while continuar == "s":
                    codigo = input("Ingrese código del producto: ").strip()
                    nuevo_precio_input = input("Ingrese nuevo precio: ").strip()
                    while not validar_entero_positivo(nuevo_precio_input):
                        print("El precio debe ser un número entero positivo.")
                        nuevo_precio_input = input("Ingrese nuevo precio: ").strip()
                    
                    nuevo_precio = int(nuevo_precio_input)
                    if actualizar_precio(productos, stock, codigo, nuevo_precio):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                    
                    continuar = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                    while not validar_si_no(continuar):
                        print("Por favor, ingrese 's' o 'n'.")
                        continuar = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
            case 4:
                
                while True:
                    codigo = input("Ingrese código del producto: ").strip()
                    if validar_codigo(productos, codigo):
                        break
                    print("El código no puede estar vacío o ya existe.")

                while True:
                    nombre = input("Ingrese nombre: ").strip()
                    if validar_texto(nombre):
                        break
                    print("El nombre no puede estar vacío.")

                while True:
                    categoria = input("Ingrese categoría: ").strip()
                    if validar_texto(categoria):
                        break
                    print("La categoría no puede estar vacía.")

                while True:
                    marca = input("Ingrese marca: ").strip()
                    if validar_texto(marca):
                        break
                    print("La marca no puede estar vacía.")

                while True:
                    peso_input = input("Ingrese peso (kg): ").strip()
                    if validar_peso(peso_input):
                        break
                    print("El peso debe ser un número mayor que cero.")

                while True:
                    es_importado_input = input("¿Es importado? (s/n): ").strip()
                    if validar_si_no(es_importado_input):
                        break
                    print("Debe indicar si es importado con 's' o 'n'.")

                while True:
                    es_para_cachorro_input = input("¿Es para cachorro? (s/n): ").strip()
                    if validar_si_no(es_para_cachorro_input):
                        break
                    print("Debe indicar si es para cachorro con 's' o 'n'.")

                while True:
                    precio_input = input("Ingrese precio: ").strip()
                    if validar_entero_positivo(precio_input):
                        break
                    print("El precio debe ser un número entero mayor que cero.")

                while True:
                    unidades_input = input("Ingrese unidades: ").strip()
                    if validar_entero_no_negativo(unidades_input):
                        break
                    print("Las unidades deben ser un número entero mayor o igual a cero.")

                
                peso_kg = float(peso_input)
                es_importado = convertir_si_no_a_booleano(es_importado_input)
                es_para_cachorro = convertir_si_no_a_booleano(es_para_cachorro_input)
                precio = int(precio_input)
                unidades = int(unidades_input)
                
                agregar_producto(productos, stock, codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades)
                print("Producto agregado con éxito.")
                
            case 5:
                codigo = input("Ingrese código del producto a eliminar: ").strip()
                if eliminar_producto(productos, stock, codigo):
                    print("Producto eliminado")
                else:
                    print("El código no existe")
            case 6:
                print("Programa finalizado.")
                break

if __name__ == "__main__":
    main()
