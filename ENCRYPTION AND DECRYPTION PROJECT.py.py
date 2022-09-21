#importing modules
from tkinter import *
import random

otp = 0

#defining fuction to generate otp
def generatekey():
    otp = 0
    otp = random.randint(1000,9999)
    text=e1.get()
    output.set(str(otp))
    encrypt(text, otp)

#defining function to encrypt data
def encrypt(text, otp):

    sum = 0 
    while otp > 0:
        sum= sum + otp%10
        otp=otp//10
    result = ""

    for i in range(len(text)):
      char = text[i]
      if (char.isupper()):
         result += chr((ord(char) + sum - 65) % 26 + 65)
      elif (char.islower()):
         result += chr((ord(char) + sum - 97) % 26 + 97)
      else:
          result += char
    l4.config(text=result)
 
#defining function to decrypt data
def decrypt(text):
    otp=int(e2.get())
    sum = 0 
    while otp > 0:
        sum= sum + otp%10
        otp=otp//10

    result = ""

    for i in range(len(text)):
      char = text[i]
      if (char.isupper()):
         result += chr((ord(char) - sum-65) % 26 + 65)
      elif (char.islower()):
         result += chr((ord(char) - sum - 97) % 26 + 97)
      else:
          result += char
    l6.config(text=result)

#main function

master = Tk()
master.title("Text Based Encryption/Decryption")
master.geometry("360x240")

lowerframe = Frame(master)
lowerframe.pack(side=BOTTOM)

done = Button(lowerframe,text="Encrypt", fg='red', command=lambda: generatekey() )
done.pack(side=BOTTOM)

dec = Button(lowerframe,text="Decrypt", fg='red', command=lambda: decrypt(e1.get()) )
dec.pack(side=BOTTOM)


topframe = Frame(master)
topframe.pack()

l1=Label(topframe, text='Enter your text for encryption/decryption ')
l1.grid(row=0, column=0)
e1 = Entry(topframe)
e1.grid(row=0,column=1)

l2=Label(topframe, text='Your OTP ')
l2.grid(row=1, column=0)
output = StringVar()
e2 = Entry(topframe,textvariable=output)
e2.grid(row=1,column=1)

l3=Label(topframe, text="Encrypted text ",anchor="w")
l3.grid(row=2, column=0)
l4=Label(topframe, text='')
l4.grid(row=2, column=1)

l5=Label(topframe,text = "Decrypted Text ", anchor="w")
l5.grid(row=3, column=0)
l6=Label(topframe, text='')
l6.grid(row=3, column=1)

master.mainloop()
