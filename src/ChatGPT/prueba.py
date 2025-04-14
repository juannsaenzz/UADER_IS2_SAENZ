"""Este módulo permite interactuar con la API de chatGPT desde consola."""

import os
from openai import OpenAI

try:
    # Habilitar historial con flecha arriba
    import readline

    LAST_INPUT = ""

    while True:
        try:
            # Nivel 1: Aceptación de consulta del usuario
            consulta = input("Escribí tu consulta para chatGPT (Enter para salir): ").strip()

            if consulta == "":
                print("Saliendo del programa.")
                break

            # Guardar en historial (habilita flecha ↑)
            readline.add_history(consulta)
            LAST_INPUT = consulta

            try:
                # Nivel 2: Tratamiento de la consulta
                if not consulta:
                    raise ValueError("No se ingresó ninguna consulta.")

                print(f"You: {consulta}")

                try:
                    # Nivel 3: Llamado a la API
                    client = OpenAI(api_key=os.getenv("sk-proj-Sp2G6CiAiSb60atBfJu3adZ" \
                    "kCB_OMnlCr6ssztdlcOYyR4_Vvb6FnhD5NZIuU" \
                    "XmYVFkPPh5TrUT3BlbkFJhxQ0KlH8CZpGtAHQz-3vyXKqNHo-SxOVBSe5q" \
                    "JkgLSkW2hJqjG2mWYT3n1Uc8b4LiymuqybVUA"))

                    response = client.chat.completions.create(
                        model="gpt-4.1",  # Usar el modelo que tengas disponible
                        messages=[
                            {"role": "user", "content": consulta}
                        ]
                    )

                    print("chatGPT:", response.choices[0].message.content.strip())

                except Exception as e:
                    print("❌ Error al invocar la API de OpenAI:", str(e))

            except ValueError as ve:
                print("⚠️ Error en la consulta:", ve)
            except Exception as e:
                print("❌ Error inesperado en el tratamiento de la consulta:", str(e))

        except Exception as e:
            print("❌ Error al leer la entrada del usuario:", str(e))

except ImportError:
    print("❌ No se pudo importar readline. En Windows, instalá pyreadline3 con:")
    print("    pip install pyreadline3")

# jhdhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# gggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# ggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# gggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# gggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# ggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# gggggggggggggggggggggggggggggggggggggggggggggggggggggg
# gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# ggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
# gggggggggggggggggggggggggggggggggggggggggggggggggggggggg
