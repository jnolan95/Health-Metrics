import garth
from getpass import getpass
from garth.exc import GarthException

# Attempts to resume a session based on tokens in the specified file.
# If the resuming is unsuccessful, triggers function authenticate, prompting user for email and password.
def resume_session():
    try:
        garth.resume("login_files/garmin_login_files/garmin_tokens")
    except:
        authenticate()

    try:
        garth.client.username
    except GarthException:
        print("Garmin session is expired. You'll need to log in again")
        authenticate()

def authenticate():
    email = input("Enter email address: ")
    password = getpass("Enter password: ")
    # If there's MFA, you'll be prompted during the login
    garth.login(email, password)

    garth.save("login_files/garmin_login_files/garmin_tokens")







