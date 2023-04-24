import speech_recognition as sr
import webbrowser


r = sr.Recognizer()
with sr.Microphone() as source:

    r.adjust_for_ambient_noise(source)
    print("Скажите что-нибудь:")

    audio = r.listen(source)


try:
    query = r.recognize_google(audio, language="ru-RU")
    print(f"Вы сказали: {query}")


    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

except sr.UnknownValueError:
    print("Не удалось распознать речь")
except sr.RequestError as e:
    print(f"Ошибка при запросе к сервису распознавания речи; {e}")


