## IMPORTS
import smtplib
import ssl
import getpass
import lorem

## PRINT START SCREEN
print("__________         _________")
print("\______   \___.__./   _____/__________    ____")
print(" |     ___<   |  |\_____  \____ \__  \  /     \ " )
print(" |    |    \___  |/        \  |_> > __ \|  Y Y \ ")
print(" |____|    / ____/_______  /   __(____  /__|_|  /")
print("           \/            \/|__|       \/      \/")
print("------------------------------------------------")
print()
print("NOTE: ONLY USE THROWAWAY GMAIL ACCOUNT!")
print("      ACTIVATE ACCESS OF LESS SECURE APPS!")
print() 

port = 456

user_login = str(input("Please enter your email adress: "))
user_pw = str(getpass.getpass("Please enter your password: "))

try:
    print("CONNECTING TO GMAIL SERVER...")
    server = smtplib.SMTP_SSL('smtp.gmail.com')
    print("CONNECTION ESTABLISHED!")
    print("LOGGING IN TO GMAIL ACCOUNT...")
    server.login(user_login, user_pw)
    print("LOGIN SUCCESSFULL!")

    target_addr = str(input("Enter target email adress!: "))
    count = int(input("Enter number of emails to send!: "))

    for i in range(count):   
        email_text = str(lorem.paragraph() + lorem.paragraph() + lorem.paragraph() + lorem.paragraph())                          
        server.sendmail(user_login, target_addr, email_text)
    server.close()

except:
    print('Something went wrong!')
