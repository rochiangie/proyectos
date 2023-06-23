def evaluar_decision():
    nombre = input("¡Hola! Por favor, ingresa tu nombre: ")
    print(f"Bienvenido, {nombre}.")

    estado_animo = input("¿Cómo te sientes en este momento? (1: Muy mal, 5: Neutral, 10: Muy bien): ")
    estado_animo = int(estado_animo)

    if estado_animo < 1 or estado_animo > 10:
        print("Opción inválida. Por favor, selecciona un número entre 1 y 10.")
        return

    if estado_animo <= 3 or estado_animo >= 8:
        print("Tu estado de ánimo no es óptimo. Quizás no sea el mejor momento para tomar decisiones importantes.")
        print(f"Espero que te sientas mejor, {nombre}. ¡Cuídate!")
    else:
        print("Tu estado de ánimo es bueno. Vamos a evaluar tu decisión.")

        respuestas = {}

        preguntas = [
            "¿Cuál es la decisión que estás considerando?",
            "¿Cuáles son las opciones que tienes?",
            "¿Qué tan importante es esta decisión para ti?",
            "¿Cuáles son los posibles resultados de cada opción?",
            "¿Has considerado los riesgos y beneficios de cada opción?",
        ]

        for pregunta in preguntas:
            respuesta = input(pregunta + " ")
            respuestas[pregunta] = respuesta

        # Generar una oración coherente con las respuestas del usuario
        oracion = f"{nombre}, estás considerando la decisión de {respuestas[preguntas[0]]}. "
        oracion += f"Tus opciones son: {respuestas[preguntas[1]]}. "
        oracion += f"Esta decisión es importante para ti y has considerado los siguientes posibles resultados: {respuestas[preguntas[3]]}. "
        oracion += f"También has evaluado los riesgos y beneficios de cada opción: {respuestas[preguntas[4]]}."

        print(oracion)

        # Evaluar si la decisión será correcta o no
        decision_correcta = True  # Ejemplo: Supongamos que la decisión siempre es correcta en este caso

        if decision_correcta:
            print("Basado en tus respuestas, considero que tu decisión será correcta. ¡Buena suerte!")
        else:
            print("Basado en tus respuestas, considero que tu decisión puede no ser la más adecuada en este momento.")

        print(f"¡{nombre}, te deseo mucho éxito en tu decisión! ¡Que te vaya muy bien!")

evaluar_decision()
