# reddit-comment-scraper
Scrapes a thread for comments and prints them out in the console

# Dependencies
To quickly install dependencie srun:

`pip install -r requirements.txt`

# reddit JSON configuration file
A JSON configuration file must be passed to the program to actually connect to reddit. It follows the format:
```
{
    "client_id": "PERSONAL_USE_SCRIPT_14_CHARS",
    "client_secret": "SECRET_KEY_27_CHARS",
    "user_agent": "YOUR_APP_NAME",
    "username": "YOUR_REDDIT_USER_NAME",
    "password": "YOUR_REDDIT_LOGIN_PASSWORD"
}
```
`client_id` , `client_secret`, and `user_agent` are all obtained from [creating an app on reddit](https://www.reddit.com/prefs/apps)

`username` and `password` are the credientials of someone added as an `developer` on the app