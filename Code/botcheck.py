import botometer
import csv

# api keys and information for authentication
rapidapi_key = ""
twitter_app_auth = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': '',
}

# creating instance of botometer API
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# to hold all usernames
accounts = []


# file where output will be stored
f = open('botstuff.txt', 'a')

# reading through file with tweets to get usernames
with open('Consolidated.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # if header row, then move on
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            # getting account username
            accounts.append(row[0])
            line_count += 1


# # Check a sequence of accounts
for screen_name, result in bom.check_accounts_in(accounts):
    # if user tweets mainly in english, get english bot score
    if result['user']['majority_lang'] == 'en':
        print(str(result['display_scores']['english']['overall']))
    # else get universal bot score
    else:
        print(str(result['display_scores']['universal']['overall']))
    print(result)
    # delimiter
    # previously was printing to csv, but now just printing
