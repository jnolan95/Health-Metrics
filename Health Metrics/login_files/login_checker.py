import login_files.fitbit_login_files.fitbit_class as fitbit_class
import login_files.fitbit_login_files.fitbit_login as fitbit_login
from fitbit.exceptions import HTTPUnauthorized
from login_files.garmin_login_files.garmin_login_resume import resume_session
import sys

# Checks both Garmin and Fitbit to ensure tokens are active/current.
# If either is not current, will prompt user for login username/password (Garmin), or direct user to Fitbit website for re-authorization

# FITBIT
    #
def check_login():
    try:
        # Attempts to execute
        fitbit_class.fitbit.user_profile_get()
    except HTTPUnauthorized:
        fitbit_login.gather_keys_oauth2()
        sys.exit("Fitbit needs reauthorization. Run again.")

    # Checks Garmin/garth for login credentials and if necessary asks for log-in info again
    resume_session()


# Can be placed as input in user_profile_get incase something getws m
# user_id="BM29Z3"