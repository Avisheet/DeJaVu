import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Attempt online recognition with Google
        text = recognizer.recognize_google(audio)
        print(f"Recognized (Google): {text}")
        return text
    except sr.UnknownValueError:
        print("Google could not understand audio")
        return None
    except sr.RequestError:
        print("Google request failed, falling back to offline recognition")

        # Fallback to offline recognition using PocketSphinx
        try:
            text = recognizer.recognize_sphinx(audio)
            print(f"Recognized (Offline Sphinx): {text}")
            return text
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
            return None
        except sr.RequestError:
            print("Sphinx request failed; check your installation")
            return None

if __name__ == "__main__":
    while True:
        recognized_text = recognize_speech()
        if recognized_text:
            print(f"Final recognized text: {recognized_text}")