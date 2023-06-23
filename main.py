

from datetime import date, time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pyautogui as pag    
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

def login(driver):
    username = driver.find_element(By.ID, "username")
    time.sleep(random.randint(1, 10))
    username.send_keys(email.get())
    time.sleep(random.randint(1, 10))

    password = driver.find_element(By.ID, "password")
    password.send_keys(passwordi.get())
    time.sleep(random.randint(1, 10))

    driver.find_element(By.TAG_NAME, 'button').click()


def goto_network(driver):

    time.sleep(random.randint(1, 10))
    driver.find_element(By.LINK_TEXT, 'My Network').click()
    time.sleep(random.randint(1, 10))


def send_requests(driver):
    driver.maximize_window()
    n = 200
    for i in range(0, n):
        print(f"doing {i}th iteration")

        #This is to close the message box appearing on the screen
        pag.click(1869, 298) 
        time.sleep(random.randint(1, 10))

        print("ROW-1") #The 5 clicks are for the 5 connection requests

        pag.click(781, 708)
        time.sleep(random.randint(1, 10))

        pag.click(1032, 708)
        time.sleep(random.randint(1, 10))

        pag.click(1280, 708)
        time.sleep(random.randint(1, 10))

        pag.click(1500, 708)
        time.sleep(random.randint(1, 10))

        print("SLIDER") #To slide down the page
        pag.click(1908, 522)
        time.sleep(random.randint(1, 10))

        print("ROW-2") #To send the next 5 connection requests
        pag.click(781, 300)
        time.sleep(random.randint(1, 10))

        pag.click(1032, 300)
        time.sleep(random.randint(1, 10))

        pag.click(1280, 300)
        time.sleep(random.randint(1, 10))

        pag.click(1500, 300)
        time.sleep(random.randint(1, 10))

        time.sleep(random.randint(1, 10))

        pag.click(105, 62) #Coordinate of reload button
        time.sleep(random.randint(1, 10)) 

        time.sleep(random.randint(1, 10))
    print("Done !")


def main():


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in"
    time.sleep(random.randint(1, 10))

    driver.get(url)
    print("Opened LinkedIn")
    time.sleep(random.randint(1, 10))
    driver.maximize_window()
    login(driver)
    time.sleep(random.randint(1, 10))
    time.sleep(random.randint(1, 10))
    goto_network(driver)
    time.sleep(random.randint(1, 10))
    send_requests(driver)


def startthebot():

    print("Email: ", email.get())
    print("PWD: ", passwordi.get())
    main()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = main_screen.winfo_screenwidth()
    height = main_screen.winfo_screenheight()

    main_screen.geometry("%dx%d" % (width, height))
    # main_screen.geometry("400x400")
    main_screen.configure(background="black")
    main_screen.title("Automate LinkedIn Connection Request")
    Art = 'LinkedInConnectBot'
    Label(text=Art, background="black", foreground="white",
          width="300", height="3", font=("Cursive", 60)).pack()
    Label(text="", background="black").pack()

    global email
    global passwordi
    email = StringVar()
    passwordi = StringVar()

    Label(text="Please Enter Your Credentials Below: ", background="black",
          foreground="white", width="30", height="2", font=("Calibri", 20)).pack()
    Label(text="", background="black").pack()
    Label(text="", background="black").pack()

    email_label = Label(text="Email Address: ", background="black",
                        foreground="white", width="30", height="2", font=("Calibri", 20))
    email_label.pack()

    email_entry = Entry(textvariable=email, width="30", font=("Calibri", 20))
    email_entry.pack()

    Label(text="", background="black").pack()
    Label(text="", background="black").pack()
    Label(text="Password: ", background="black", foreground="white",
          width="30", height="2", font=("Calibri", 20)).pack()

    password_entry = Entry(textvariable=passwordi,
                           width="30", font=("Calibri", 20))
    password_entry.pack()

    Label(text="", background="black").pack()

    b3 = Button(text="GET STARTED", height="2", width="30",
                activebackground="black", command=startthebot, bg='white').pack()
    main_screen.after(15000, lambda: main_screen.destroy())
    main_screen.mainloop()


main_account_screen()
