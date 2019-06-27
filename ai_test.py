import speech_recognition as sp
import pyttsx3

### set an object for my recognizer ###
speech = sp.Recognizer()

### set up an object for my pyttsx engine ### 
engine = pyttsx3.init()

### get the properties from the engine ###
voices = engine.getProperty('voices')
voice = engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

### get the voice rate ###
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

### function that says the commands ###
def respond_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

### function that listens to what you are saying ###
def read_cmd():
    #initiate an empty voice_text 
    voice_text =''
    print('Listening...')

    ## the source where the voice is coming from ###
    with sp.Microphone() as source:
        audio = speech.listen(source= source,timeout=10,phrase_time_limit=5) #the audio is the sound that is picked up from the mic

        try:
            voice_text = speech.recognize_google(audio)
        except sp.UnknownValueError:
            pass
        except sp.RequestError as e:
            print(e)
        except sp.WaitTimeoutError:
            pass
        return voice_text

### run this before anything else ###
if __name__ == '__main__':
    respond_cmd('Hello. My name is Nana. Your A.I')

    while True:
        voice_note = read_cmd()
        print('audo picked up: {}'.format(voice_note))

        ## list of commands that am going to issue out ##
        if 'hello' in voice_note:
            respond_cmd('Hello Musonda. how can i be of assistance')
            continue
        if 'call girlfriend' in voice_note:
            respond_cmd('Sure thing. But am still an A.I i do not have a number yet')
            continue
        if 'bye' in voice_note:
            respond_cmd('bye bye. see you next time')
            exit()
