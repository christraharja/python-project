import speech_recognition as sr
# Declaring the main function below
def main():
    x = sr.Recognizer()

    with sr.Microphone() as sources:
        x.adjust_for_ambient_noise(sources)
        # asking the user to start the speech
        print("Start recording: say something")

        audioSystem = x.listen(sources)
        # Loading
        print("Loading, recognizing Now .... ")

        # recognize speech based on google system
        # throwing try and catch statement
        try:
            print("You have said \n" + x.recognize_google(audioSystem))
            print("Audio Recorded Successfully \n ")


        except Exception as a:
            print("Error :  " + str(a))

        # write audio down here

        with open("recorded.wav", "wb") as b:
            b.write(audioSystem.get_wav_data())


if __name__ == "__main__":
    main()











