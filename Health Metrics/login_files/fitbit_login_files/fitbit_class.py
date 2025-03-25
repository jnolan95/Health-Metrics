import fitbit
import json

# Opens JSON file Oauth information is stored at. Saves info as a dictionary.
with open("login_files/fitbit_login_files/fitbit_oauth.json") as json_file:
    oauth = json.load(json_file)

# Variable fitbit. Stored in this variable is 
fitbit = fitbit.Fitbit(
    client_id= oauth["client_id"],
    client_secret= oauth["client_secret"],
    access_token= oauth["access_token"],
    refresh_token= oauth["refresh_token"],
    expires_in = oauth["expires_in"]
)








