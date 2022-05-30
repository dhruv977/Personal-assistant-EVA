import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import smtplib
import shutil
import ctypes
import winshell
from email.message import EmailMessage
from selenium import webdriver
import os
import wolframalpha
import subprocess
from tkinter import *
import requests
import threading

class AppGui:
    def __init__(self):

        window = Tk()
        window.title("Eva")
        window.geometry("300x300")
        l1 = Label(window, text="Eva", width=300, bg="black", fg="white", font=("Calibri", 13)).pack()
        microphone_photo = PhotoImage(file="mic.png")
        microphone_button = Button(image=microphone_photo, command=clicked)
        microphone_button.pack(pady=10)
        window.mainloop()


def clicked():
    os.system('python Eva.py')


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    # This Function will clean any
    # command before execution of this python file
    clear()
    ui = AppGui()



