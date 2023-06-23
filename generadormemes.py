import requests

def obtener_chiste_humor_negro():
    url = "https://v2.jokeapi.dev/joke/Dark?type=single"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data["type"] == "single":
        return data["joke"]
    else:
        return None

def main():
    print("Bienvenido al generador de chistes de humor negro.")
    print("A continuación, te mostraré un chiste:")

    chiste = obtener_chiste_humor_negro()

    if chiste:
        print(chiste)
    else:
        print("No se pudo obtener un chiste en este momento. Inténtalo más tarde.")

    print("Gracias por utilizar el generador de chistes de humor negro.")

if __name__ == '__main__':
    main()

otra_variable = "Solo ejemplo"