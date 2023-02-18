import pyttsx3 as voz
import speech_recognition as sr
import subprocess as sub
from datetime import datetime
import pywhatkit
import wikipedia

# Configuración de la voz del asistente
voice = voz.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[0].id)
voice.setProperty('rate', 140)

wikipedia.set_lang("es")


def say(text):
    voice.say(text)
    voice.runAndWait()


while True:

    recognizer = sr.Recognizer()
    # Activar micrófono
    with sr.Microphone() as source:
        print('Escuchando...')
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:  # Si se entiende nuestra petición entramos a la lógica principal
        comando = recognizer.recognize_google(audio, language='es')
        print(f'Creo que dijiste "{comando}"')

        comando = comando.lower()
        comando = comando.split(' ')

        if 'asistente' in comando:

            if 'abre' in comando or 'abrir' in comando:

                sites = {
                    'google': 'google.com',
                    'youtube': 'youtube.com',
                    'instagram': 'instagram.com',
                    'spotify': 'open.spotify.com'

                }

                for i in list(sites.keys()):
                    print(comando)
                    if i in comando:
                        sub.call(f'start Chrome.exe {sites[i]}', shell=True)
                        say(f'Abriendo {i}')

            elif 'reproduce' in comando:

                pywhatkit.playonyt(comando)

            elif 'hora' in comando:
                time = datetime.now().strftime('%H:%M')
                say(f'Son las {time}')

            elif 'fecha' in comando:
                fecha = datetime.now().strftime('Día :%d, Mes: %m, Año: %Y ')
                say('Hoy estamos: ' + fecha)

            elif 'termina' in comando or 'terminar' in comando or 'término' in comando or 'terminó' in comando:
                say('Sesión finalizada')
                break

            elif 'quien' or 'quién' in comando:

                info = wikipedia.summary(comando, 1)
                print(info)
                say(info)

    except:  # Si no se entiende nos dará este mensaje
        print('No te entendí, por favor vuelve a intentarlo')
       
