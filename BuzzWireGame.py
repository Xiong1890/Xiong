
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT) #LED
GPIO.setup(7,GPIO.IN) #wire and loop
GPIO.setup(16,GPIO.IN) # button


print ("Press the button to begin!")


while GPIO.input(16)==0:
    pass #Pass is a null operation

print ("Now try your luck! Then press the button to end.")

#wait for debounce before beginning
time.sleep(0.5)

#counter
score = 0

#while loop until button pressed
while GPIO.input(16) == 0:
    if GPIO.input(7) == 1:
        #turn on LED and increment counter      
        GPIO.output(18,True)
        score = score + 1
    elif GPIO.input(7) == 0:
        # turn off LED
        GPIO.output(18,False)
    time.sleep(0.3)    

#print the score.
print ("You scored", score)

if score == 0:
    print ("Which is amazing")
if score >=1 and score <=3:
    print ("Which is not bad")
if score >3:
    print ("Which is terrible")
GPIO.cleanup()
