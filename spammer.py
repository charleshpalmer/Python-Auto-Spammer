import pyautogui, time #Importing the AutoGUI module and the Time.

time.sleep(7) #Setting the ammount of time the program will sleep for before beginning to type.

f = open("read.txt", 'r') #Saving the file "read.txt" to varibable 'F'.

for word in f: #For every word in the "read.txt" file.

    pyautogui.typewrite(word) #Type that word.

    pyautogui.press("enter") #Press enter key on keyboard.



