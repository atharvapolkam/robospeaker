import gtts
import playsound
while True:

    print("welcome to Robospeaker 1.1 created by ATHARVA")
    text=input("enter something here:")
    sound = gtts.gTTS(text, lang="en")
    sound.save("welcome.mp3")
    playsound.playsound("welcome.mp3")
    if(text=="end"):
        break







    continue




