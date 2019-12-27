
# Emo Band Lyrics
Twitter bot to generate new lyrics inspired by emo bands using a Markov chain. Lyrics are aggregated by fetching the top five songs using [LyricsGenius](https://github.com/johnwmillr/LyricsGenius). 

## Requirements
 - Twitter developer account
 - tweepy (bot.py)
 - numpy (chain.py)

Optional:
 - Genius dev account
 - lyricsgenius (lyrics.py)
 - PythonAnywhere (hosting) 

## Setup
After cloning the repo in a PythonAnywhere bash window, create `credentials.py` to store `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_KEY`, and `ACCESS_SECRET` from your twitter app as strings. Optionally, store `GENIUSKEY` if you would like to compile your own dictionary, requiring you to `pip install lyricsgenius`. In the bash window, `python bot.py` will run the bot.

**credentials.py**:
```Python
CONSUMER_KEY = 'twitter consumer key'
CONSUMER_SECRET = 'twitter consumer private key'
ACCESS_KEY = 'twitter access key'
ACCESS_SECRET = 'twitter access private key'
GENIUSKEY = 'genius key' # optional
```

## Usage
Once the bot is set up, it is fairly maintenance free. In order to add more lyrics, append artists.txt with desired artists. Then, run lyrics.py to generate a new dictionary. This process may take some time. After a new dictionary is made, run crate_chain.py to update the json file containing the chain. In create_chain.py, adjusting `LENGTH` will adjust the like-ness of keys stored in the Markov chain. Higher values will create more drastically unoriginal lyrics.

## References
[How to write a twitter bot with python and tweepy](https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/)

[Build a Markov Chain Sentence Generator in 20 lines of Python](https://www.jeffcarp.com/posts/2019/markov-chain-python/)
