# BeginsWithU

## Summary
With social media networks connecting people all over the world on a daily basis, people can openly talk about
important issues. BeginsWithU allows users, who are interested in a specific issue, to access informative
articles and discover charities to help change the world.

## Instructions
- Install python3 and pip
- Clone Repository
- Create a venv using these instructions : https://docs.python.org/3/library/venv.html
- Upon activation of venv, install packages from requirements.txt using this command :
```
pip install -r requirements.txt 
```
- Run trending.py from the utils folder and then run charity.py
- Run bot.py and tweet "how to help" @bwuhelpbot and wait a minute for it to reply with a link.
- Run app.py to see extra information

## Features
- Gathers twitter trends and uses natural language processing(via the vader package) to see peoples feeling towards a trend
- Naively isolates keywords from tweets for retrieving charity data
- Naively searches for charities and other information related to trend
- The bot provides people with links previously gathered
- The Flask app does some visualization and displays bots tweets

## Known Bugs
- There won't always be trending topics that require attention so thats why we have a test case text file
- The search for charities is still naive and needs to be improved before completely deploying the bot
- Tweets in foreign languages causes gaps in data
- We use limited data to make it usable for the hackathon, more optimization and more data will be needed for later.
