#import libraries
import customtkinter as ctk
import speech_recognition as sr
import pyttsx3 as tts

#define theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

#main frame
root = ctk.CTk()
root.title("Talkulator")
root.geometry("420x640")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=False)

# Initialize a global variable for the current input
current_input = ""

def vo():
    global current_input
    # Create an instance of the recognizer
    r = sr.Recognizer()

    # Use the microphone as source
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    # Convert speech to text
    try:
        text = r.recognize_google(audio).lower()
        c = text.replace("x", "into").replace("-", "minus").replace("plus", "+")
        text = text.replace("one", "1")
        text = text.replace("x", "*").replace("multiplied by", "*").replace("into", "*")
        text = text.replace("raised to the power", "**").replace("raise to the power", "**")
        text = text.replace("to the power", "**").replace("raised to", "**").replace("raise to", "**")
        a= text + " = " + str(eval(text))
        c= c + " = " + str(eval(text))
        print(a)
        txt(a)

        speech = tts.init()
        speech.say(c)
        speech.runAndWait()

    except sr.UnknownValueError:
        txt("Could not understand audio")
    except sr.RequestError:
        txt("Could not request results from Google Speech Recognition service")

def append_to_input(value):
    global current_input
    current_input += value
    txt(current_input)

def evaluate():
    global current_input
    try:
        result = eval(current_input)
        txt(f"{current_input} = {result}")
        current_input = ""  # Clear input after evaluation
    except Exception as e:
        txt("Error in calculation")
        current_input = ""  # Clear input on error

#fonts
font1 = ("Helvetica", 18,"bold")
font2 = ("Helvetica", 42, "bold")
font3 = ("Helvetica", 18)
font4 = ("Helvetica", 12, "bold")

#graffiti
title = ctk.CTkLabel(master=frame, text="Talkulator - The Accessible Calculator", font=font1)
title.pack(pady=20, padx=18)

label = ctk.CTkLabel(master=frame, text="", height=100, font=font2, corner_radius=10)
label.pack(pady=30, ipadx=10000, padx=50)

def txt(display):
    label.configure(text=display)

#numpad frame
numpad = ctk.CTkFrame(master=frame)
numpad.pack(pady=50, padx=10, fill="both", expand=True)

#creating table
numpad.columnconfigure(0, weight=1)
numpad.columnconfigure(1, weight=1)
numpad.columnconfigure(2, weight=1)
numpad.columnconfigure(3, weight=1)

numpad.rowconfigure(0, weight=1)
numpad.rowconfigure(1, weight=1)
numpad.rowconfigure(2, weight=1)
numpad.rowconfigure(3, weight=1)
numpad.rowconfigure(4, weight=1)

#buttons
button1 = ctk.CTkButton(master=numpad, text="1", command=lambda: append_to_input("1"), height=50, width=50, corner_radius=10, font=font3)
button1.grid(row=1, column=0, padx=2, pady=2, sticky="news")

button2 = ctk.CTkButton(master=numpad, text="2", command=lambda: append_to_input("2"), height=50, width=50, corner_radius=10, font=font3)
button2.grid(row=1, column=1, padx=2, pady=2, sticky="news")

button3 = ctk.CTkButton(master=numpad, text="3", command=lambda: append_to_input("3"), height=50, width=50, corner_radius=10, font=font3)
button3.grid(row=1, column=2, padx=2, pady=2, sticky="news")

button4 = ctk.CTkButton(master=numpad, text="4", command=lambda: append_to_input("4"), height=50, width=50, corner_radius=10, font=font3)
button4.grid(row=2, column=0, padx=2, pady=2, sticky="news")

button5 = ctk.CTkButton(master=numpad, text="5", command=lambda: append_to_input("5"), height=50, width=50, corner_radius=10, font=font3)
button5.grid(row=2, column=1, padx=2, pady=2, sticky="news")

button6 = ctk.CTkButton(master=numpad, text="6", command=lambda: append_to_input("6"), height=50, width=50, corner_radius=10, font=font3)
button6.grid(row=2, column=2, padx=2, pady=2, sticky="news")

button7 = ctk.CTkButton(master=numpad, text="7", command=lambda: append_to_input("7"), height=50, width=50, corner_radius=10, font=font3)
button7.grid(row=3, column=0, padx=2, pady=2, sticky="news")

button8 = ctk.CTkButton(master=numpad, text="8", command=lambda: append_to_input("8"), height=50, width=50, corner_radius=10, font=font3)
button8.grid(row=3, column=1, padx=2, pady=2, sticky="news")

button9 = ctk.CTkButton(master=numpad, text="9", command=lambda: append_to_input("9"), height=50, width=50, corner_radius=10, font=font3)
button9.grid(row=3, column=2, padx=2, pady=2, sticky="news")

button0 = ctk.CTkButton(master=numpad, text="0", command=lambda: append_to_input("0"), height=50, width=50, corner_radius=10, font=font3)
button0.grid(row=4, column=1, padx=2, pady=2, sticky="news")

buttonp = ctk.CTkButton(master=numpad, text="+", command=lambda: append_to_input("+"), height=50, width=50, corner_radius=10, font=font3)
buttonp.grid(row=0, column=3, padx=2, pady=2, sticky="news")

buttonm = ctk.CTkButton(master=numpad, text="-", command=lambda: append_to_input("-"), height=50, width=50, corner_radius=10, font=font3)
buttonm.grid(row=1, column=3, padx=2, pady=2, sticky="news")

buttoni = ctk.CTkButton(master=numpad, text="*", command=lambda: append_to_input("*"), height=50, width=50, corner_radius=10, font=font3)
buttoni.grid(row=2, column=3, padx=2, pady=2, sticky="news")

buttond = ctk.CTkButton(master=numpad, text="/", command=lambda: append_to_input("/"), height=50, width=50, corner_radius=10, font=font3)
buttond.grid(row=3, column=3, padx=2, pady=2, sticky="news")

# New buttons for parentheses
buttonbo = ctk.CTkButton(master=numpad, text="(", command=lambda: append_to_input("("), height=50, width=50, corner_radius=10, font=font3)
buttonbo.grid(row=4, column=0, padx=2, pady=2, sticky="news")

buttonbc = ctk.CTkButton(master=numpad, text=")", command=lambda: append_to_input(")"), height=50, width=50, corner_radius=10, font=font3)
buttonbc.grid(row=4, column=2, padx=2, pady=2, sticky="news")

buttoneq = ctk.CTkButton(master=numpad, text="=", command=evaluate, height=50, width=50, corner_radius=10, font=font3)
buttoneq.grid(row=4, column=3, padx=2, pady=2, sticky="news")

buttonac = ctk.CTkButton(master=numpad, text="AC", command=lambda: [txt(""), reset_input()], height=50, width=50, corner_radius=10, font=font4)
buttonac.grid(row=0, column=0, padx=2, pady=2, sticky="news")

buttondeci = ctk.CTkButton(master=numpad, text=".", command=lambda: append_to_input("."), height=50, width=50, corner_radius=10, font=font3)
buttondeci.grid(row=0, column=1, padx=2, pady=2, sticky="news")

buttonvo = ctk.CTkButton(master=numpad, text="VI", command=vo, height=50, width=50, corner_radius=10, font=font4)
buttonvo.grid(row=0, column=2, padx=2, pady=2, sticky="news")

def reset_input():
    global current_input
    current_input = ""

root.mainloop()
