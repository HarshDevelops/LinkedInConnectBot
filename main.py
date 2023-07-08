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
import logging

# Configure logging
logging.basicConfig(filename='linkedin_bot.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def login(driver):
    try:
        username = driver.find_element(By.ID, "username")
        time.sleep(random.randint(1, 10))
        username.send_keys(email.get())
        time.sleep(random.randint(1, 10))

        password = driver.find_element(By.ID, "password")
        password.send_keys(passwordi.get())
        time.sleep(random.randint(1, 10))

        driver.find_element(By.TAG_NAME, 'button').click()
    except Exception as e:
        logging.error(f"Error occurred during login: {str(e)}")
        messagebox.showerror("Error", "An error occurred during login.")

def goto_network(driver):
    try:
        time.sleep(random.randint(1, 10))
        driver.find_element(By.LINK_TEXT, 'My Network').click()
        time.sleep(random.randint(1, 10))
    except Exception as e:
        logging.error(f"Error occurred while navigating to 'My Network': {str(e)}")
        messagebox.showerror("Error", "An error occurred while navigating to 'My Network'.")

def send_requests(driver):
    try:
        driver.maximize_window()
        n = 200
        for i in range(0, n):
            logging.info(f"Performing {i}th iteration")
            pag.click(1869, 298)  # Close the message box appearing on the screen
            time.sleep(random.randint(1, 10))

            logging.info("ROW-1")  # The 5 clicks are for the 5 connection requests
            pag.click(781, 708)
            time.sleep(random.randint(1, 10))
            pag.click(1032, 708)
            time.sleep(random.randint(1, 10))
            pag.click(1280, 708)
            time.sleep(random.randint(1, 10))
            pag.click(1500, 708)
            time.sleep(random.randint(1, 10))

            logging.info("SLIDER")  # To slide down the page
            pag.click(1908, 522)
            time.sleep(random.randint(1, 10))

            logging.info("ROW-2")  # To send the next 5 connection requests
            pag.click(781, 300)
            time.sleep(random.randint(1, 10))
            pag.click(1032, 300)
            time.sleep(random.randint(1, 10))
            pag.click(1280, 300)
            time.sleep(random.randint(1, 10))
            pag.click(1500, 300)
            time.sleep(random.randint(1, 10))
            time.sleep(random.randint(1, 10))
            pag.click(105, 62)  # Coordinate of reload button
            time.sleep(random.randint(1, 10))
            time.sleep(random.randint(1, 10))

        logging.info("Done!")
    except Exception as e:
        logging.error(f"Error occurred while sending connection requests: {str(e)}")
        messagebox.showerror("Error", "An error occurred while sending connection requests.")

def main():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        url = "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in"
        time.sleep(random.randint(1, 10))
        driver.get(url)
        logging.info("Opened LinkedIn")
        time.sleep(random.randint(1, 10))
        driver.maximize_window()
        login(driver)
        time.sleep(random.randint(1, 10))
        time.sleep(random.randint(1, 10))
        goto_network(driver)
        time.sleep(random.randint(1, 10))
        send_requests(driver)
    except Exception as e:
        logging.error(f"Error occurred in the main function: {str(e)}")
        messagebox.showerror("Error", "An error occurred in the main function.")

def startthebot():
    try:
        logging.info("Email: " + email.get())
        logging.info("PWD: " + passwordi.get())
        main()
    except Exception as e:
        logging.error(f"Error occurred while starting the bot: {str(e)}")
        messagebox.showerror("Error", "An error occurred while starting the bot.")

def main_account_screen():
    try:
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
    except Exception as e:
        logging.error(f"Error occurred in the main_account_screen function: {str(e)}")
        messagebox.showerror("Error", "An error occurred in the main_account_screen function.")

main_account_screen()
