# Función que calcula un valor hash a partir de una cadena de caracteres.
def hash_funcion(valor):
    hash_valor = 0
    for char in valor:
        # Suma el valor ASCII de cada carácter en la cadena.
        hash_valor += ord(char)
    return hash_valor

# Función que encripta una cadena de caracteres utilizando un valor hash.
def encriptar_valor(valor, hash_valor):
    encriptado_valor = ""
    for char in valor:
        # Encripta el carácter sumando el valor hash al valor ASCII original.
        encriptado_char = ord(char) + hash_valor
        encriptado_valor += chr(encriptado_char)
    return encriptado_valor

# Función que desencripta una cadena de caracteres encriptada utilizando un valor hash.
def desencriptar_valor(encriptado_valor, hash_valor):
    desencriptado_valor = ""
    for char in encriptado_valor:
        # Desencripta el carácter restando el valor hash al valor ASCII encriptado.
        desencriptado_char = ord(char) - hash_valor
        desencriptado_valor += chr(desencriptado_char)
    return desencriptado_valor


def main():
    # Imprime los nombres de los integrantes del equipo.
    print("\t\tIntegrantes del equipo:\n\t* Garcia Mayorga Brayan Jair\n\t* Camacho Garcia Julia Guadalupe\n\t* Ramirez Vazquez Wendy Itzel\n\n")

    # Solicita al usuario ingresar una serie de valores separados por comas y los almacena en 'input_string'.
    input_string = input("Ingresa una serie de valores separados por coma: ")

    # Divide la cadena ingresada en 'input_string' en una lista de valores utilizando la coma como separador.
    values = input_string.split(',')

    # Crea tres listas vacías para almacenar los valores originales, encriptados y desencriptados.
    original_valores = list()
    encriptados_valores = list()
    desencriptados_valores = list()

    # Itera a través de cada valor en 'values'.
    for valor in values:
        # Calcula un valor hash para el valor actual.
        hash_valor = hash_funcion(valor)

        # Encripta el valor actual utilizando la función 'encriptar_valor'.
        encriptado_valor = encriptar_valor(valor, hash_valor)

        # Desencripta el valor encriptado utilizando la función 'desencriptar_valor'.
        desencriptado_valor = desencriptar_valor(encriptado_valor, hash_valor)

        # Agrega el valor original, encriptado y desencriptado a las listas correspondientes.
        original_valores.append(valor)
        encriptados_valores.append(encriptado_valor)
        desencriptados_valores.append(desencriptado_valor)

    # Imprime los valores contenidos en las listas dinámicas.
    print("Valores contenidos en las listas dinámicas")
    print("\nValores originales:")
    print(" ".join(original_valores))  # Imprime los valores originales separados por espacio.
    print("\nValores encriptados:")
    print(" ".join(encriptados_valores))  # Imprime los valores encriptados separados por espacio.
    print("\nValores desencriptados:")
    print(" ".join(desencriptados_valores))  # Imprime los valores desencriptados separados por espacio.

    # Espera a que el usuario presione Enter para cerrar la aplicación.
    input("Clic enter para cerrar")


if __name__ == "__main__":
    main()
