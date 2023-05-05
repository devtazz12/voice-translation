from django.shortcuts import render
from googletrans import Translator
from speech_recognition import Recognizer, Microphone
from gtts import gTTS
from playsound import playsound
import os


recognizer=Recognizer()
translator=Translator()

def index(request):
    voicetext="hello"
    translationText="hello"
    if request.method=="POST":
        inputlang= request.POST.get('sel-country', False)
        outlang= request.POST.get('converted-country', False)
        with Microphone() as source:
            print("speak now....")
            voice=recognizer.listen(source)
            voicetext=recognizer.recognize_google(voice, language=inputlang)
        
            translation=translator.translate(voicetext, dest=outlang)
            translationText=translation.text
            convertedAudio=gTTS(translation.text, lang=outlang)
            os.remove("otherlang.mp3")
            convertedAudio.save("otherlang.mp3")
            playsound("otherlang.mp3")
        
    
    return render(request, 'index.html', {'inputtext':voicetext, 'outputText':translationText})