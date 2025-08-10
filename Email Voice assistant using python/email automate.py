import speech_recognition as sr
import yagmail
 
recognizer= sr.Recognizer
# we are converting microphone as source
with sr.Microphone() as source:
    print('Clearing background noise:')
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print('Waiting for your message...')
    recorded_audio= recognizer.listen(source)

    try:
        print('Printing the message:')
        text=recognizer.recognize_google(recorded_audio,language='en-US')

        print('Your message:{}'.format(text))

    except Exception as ex:
        print(ex)

# Automate mails
reciever='akash022.as@gmail.com'
message=text
sender=yagmail.SMTP('shettyananth24@gmail.com')
sender.send(to=reciever,subject='This is an automated mail',contents=message)
print('Mail sent successfully!')
print('Exiting the program...')

    

