import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
import sys
import subprocess
import os

try:
    import pyaudio
except Exception as e:
    try:
        os.system("pipwin install pyaudio")
    except Exception as e:
        try:
            os.system("pip install pyaudio")
        except Exception as e:
            print("Exception occur ", e)
            print("Install pyaudio manually")
        import pyaudio

# import custom features
try:
    from AIAssistant.features.face_reco.dataset_create import DatasetCreate
    from AIAssistant.features.face_reco.train import Train
    from AIAssistant.features.face_reco.predict import Predict
    from AIAssistant.features.face_reco.open import Open
    from AIAssistant.features.send_mail import email_send
    from AIAssistant.features.setup import setup
    from AIAssistant.features.weather import weather as wea
    from AIAssistant.features.website_open import website_open
    from AIAssistant.features.date_time import date_time
    from AIAssistant.features.news import news as nw
    from AIAssistant.features.tell_me_about import tell_me_about as tma

except Exception as e:
    print("some module are missing{}".format(e))

class AIAssistant:
    def __init__(self):
        pass

    def mic_input(self):
        """
        Fetch input from mic
        :return: user's voice input as text if true, false if fail
        """
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Say something...')
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
            try:
                command = r.recognize_google(audio).lower()
                print('You said: ' + command + '\n')
            except sr.UnknownValueError:
                print('....')
                command = self.mic_input()
            return command
        except Exception as e:
            print(e)
            return False

    def text2speech(self, text):
        """
        Convert any text to speech
        :param text: text (String)
        :return: True / False (Play sound if True otherwise write exception to log and return False)
        """
        try:
            myobj = gTTS(text=text, lang='en', slow=False)
            myobj.save("tmp.mp3")
            playsound("tmp.mp3")
            os.remove("tmp.mp3")
            return True
        except Exception as e:
            mytext = "Sorry I couldn't understand, or not implemented to handle this input"
            print(mytext)
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("tmp.mp3")
            playsound("tmp.mp3")
            os.remove("tmp.mp3")
            print(e)
            return False

    def shutdown(self):
        """
        Shutdown the AIAssistant API, exit from program
        :return: if no error then exit from program, False if Fail
        """
        try:
            self.text2speech('Good bye. Have a nice day')
            sys.exit()
        except Exception as e:
            print(e)
            return False

    def website_opener(self, domain):
        """
        This will open website according to domain
        :param domain: any domain, example "youtube.com"
        :return: True if success, False if fail
        """
        return website_open.website_opener(domain)

    def tell_me_date(self):
        """
        Just return date as string
        :return: date if success, False if fail
        """
        return date_time.date()

    def tell_me_time(self):
        """
        This function will return time
        :return: Time if success, False if fail
        """
        return date_time.time()

    def weather(self, city='Indore'):
        """
        Return weather
        :param city: Any city of this world
        :return: weather info as string if True, or False
        """
        try:
            res = wea.weather_app(city)
        except Exception as e:
            print(e)
            res = False
        return res

    def news(self):
        """
        Fetch top news of the day from news.google.com/news/rss
        :return: news list of string if True, False if fail
        """
        return nw.news()

    def tell_me(self, topic='tell me about Taj Mahal'):
        """
        Tells about anything from wikipedia
        :param topic: any string is valid options
        :return: First 500 character from wikipedia if True, False if fail
        """
        return tma.tell_me_about(topic)

    def launchApp(self, face_classifier, model, path):

        obj_predict = Predict(face_classifier, model)
        obj_predict.predict()
        var1 = obj_predict.var1

        obj_open = Open()
        obj_open.luanchingApp(var1, path)

    def email(self, config_path):
        return email_send.send(config_path)

    def setup(self, config_path):
        setup.setup(config_path)

    def dataset_create(self, face_classifier, data_create):
        obj_dataset = DatasetCreate(face_classifier=face_classifier,data_create=data_create)
        obj_dataset.dataset_create()

    def train_model(self, data_path, model_path):
        obj_train = Train(data_path, model_path)
        obj_train.train()