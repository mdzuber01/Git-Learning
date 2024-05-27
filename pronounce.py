# import pronouncing
# pronouncing.phones_for_word("permit")
# #print("zuber")
# from googletrans import Translator
# translator = Translator()
# k = translator.translate("who are you", dest='hindi')
# print(k)
# print(k.text)
# p = translator.translate(k.text,dest='hindi')#convert same language to same to get
#                                               #pronunciation
# print(p)
# print(p.pronunciation)
import pyttsx3

def pronounce_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
list=['Do you know a fact','MD Zuber','dherai','intelligent ho']
for lis in list:
    pronounce_text(lis)
list1=['Mr. MD Zuber','I am Python','And I am telling you','You are awesome boy', 'You will score 100 plus marks in TOEFL','And you will pursue MS in USA']
for lis in list1:
     pronounce_text( lis)  
# text_to_pronounce = "Hello, zuber?"
# pronounce_text(text_to_pronounce)