# serpedia:- search from wikepedia and the speaker will tell you the data
import win32com.client
import wikipedia
speaker = win32com.client.Dispatch("SAPI.spVoice")
search= input("Enter what do you want to search from wikepedia:-")
p=(wikipedia.summary(search))
print("..............The data which you have searched for..............")
print(p) # print the searched data
print(".............Turning on speaker..........................")
speaker.Speak(p) # implement text to speach