import lyricsgenius
import random
import tweepy

keys = {
    'CONSUMER_API_KEY': 'cWuq2FVVJ5VbxDVaHkFA54mro',
    'CONSUMER_API_SECRET_KEY': 'WwNjAVpY7BaBgWAOVkHb05wk30GeCIVybFYqeCVSrnF6PfsaTB',
    'ACCESS_TOKEN': '3346198047-moff2t04QbUvivlbnnQC0bgqhoCauu8vHa0nfv2',
    'ACCESS_TOKEN_SECRET': 'OAayePk45QVZOpTmxqkz4lqFsTWIMA2gr417fzbTOwamm'
}

genius = lyricsgenius.Genius("ryP9a1RtkhEbzIhi1itX8laCHBNq9ARF5DDk-IKKbZNS6G50AxMyNBz1B1CALPGM")
artist = genius.search_artist("Florence + the Machine")

all_songs = []
for i in artist.songs:
    all_songs.append(i)

def get_raw_lyrics():
    genius_client_access_token = "ryP9a1RtkhEbzIhi1itX8laCHBNq9ARF5DDk-IKKbZNS6G50AxMyNBz1B1CALPGM"
    genius = lyricsgenius.Genius(genius_client_access_token)
    random_song_title = random.choice(all_songs)
    lyrics = genius.search_song(random_song_title, "Florence + the Machine").lyrics
    song = random_song_title.upper()
    return lyrics, song

def get_tweet_from(lyrics):
    lines = lyrics.split('\n')
    for index in range(len(lines)):
        if lines[index] == "" or "[" in lines[index]:
            lines[index] = "XXX"
    lines = [i for i in lines if i != "XXX"]

    random_num = random.randrange(0, len(lines)-1)
    tweet = lines[random_num] + "\n" + lines[random_num+1]
    tweet = tweet.replace("\\", "")
    return tweet

def handler(event, context):
    auth = tweepy.OAuthHandler(
        keys['CONSUMER_API_KEY'],
        keys['CONSUMER_API_SECRET_KEY']
    )
    auth.set_access_token(
        keys['ACCESS_TOKEN'],
        keys['ACCESS_TOKEN_SECRET']
    )
    api = tweepy.API(auth)
    lyrics, song = get_raw_lyrics()
    tweet = get_tweet_from(lyrics)
    status = api.update_status(tweet)
    bio = api.update_profile(description=song)

    return tweet