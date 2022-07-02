import os
import time
import tweepy
import random
import lyricsgenius

CONSUMER_API_KEY:  os.environ['CONSUMER_API_KEY']
CONSUMER_API_SECRET_KEY:  os.environ['CONSUMER_API_SECRET_KEY']
ACCESS_TOKEN:  os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET:  os.environ['ACCESS_TOKEN_SECRET']
genius_client_access_token =  os.environ['genius_client_access_token']

all_songs=["Dog Days Are Over" , "Jenny of Oldstones (Game of Thrones)" , "Shake It Out" , "Hunger" , "King" , "Delilah" ,
           "Sky Full of Song" , "Big God" , "Never Let Me Go" , "Cosmic Love" , "Patricia" , "Wish That You Were Here" , "The End of Love" ,
           "What Kind of Man" , "Seven Devils" , "Ship to Wreck" , "June" , "Queen of Peace" , "100 Years" , "How Big, How Blue, How Beautiful" ,
           "You’ve Got the Love" , "Grace" , "South London Forever" , "Third Eye" , "Free" , "No Light, No Light" , "Over the Love" ,
           "Various Storms & Saints" , "What the Water Gave Me" , "St. Jude" , "No Choir" , "Only If for a Night" , "Which Witch (Demo)" ,
           "Girl with One Eye" , "Rabbit Heart (Raise It Up)" , "My Love" , "Howl" , "Moderation" , "Spectrum" , "Girls Against God" ,
           "Light of Love" , "Mother" , "Too Much Is Never Enough" , "Bird Song" , "Dream Girl Evil" , "Caught" , "Blinding" , "Choreomania" ,
           "Long & Lost" , "Heaven Is Here" , "Cassandra" , "Kiss with a Fist" , "All This and Heaven Too" , "Heavy In Your Arms" ,
           "Drumming Song" , "Make Up Your Mind" , "Bedroom Hymns" , "Daffodil" , "Breaking Down" , "Pure Feeling" , "Between Two Lungs" ,
           "The Bomb" , "Heartlines" , "Hiding" , "Morning Elvis" , "My Boy Builds Coffins" , "Stand By Me" , "I’m Not Calling You a Liar" ,
           "Breath of Life" , "Falling" , "Back in Town" , "Hurricane Drunk" , "Lover to Lover" , "Call Me Cruella" , "Leave My Body" ,
           "Strangeness and Charm" , "Haunted House" , "As Far As I Could Get" , "Prayer Factory" , "Landscape (Demo)" , "I Will Be" ,
           "Conductor" , "Hardest of Hearts" , "Swimming" , "Remain Nameless" , "Restraint" , "I Love You All the Time" , "Third Eye (Demo)" ,
           "Take Care" , "Are You Hurting the One You Love?" , "Addicted to Love" , "Hospital Beds" , "Tiny Dancer" , "Cornflake Girl" ,
           "Spectrum (Say My Name) [Calvin Harris Remix]" , "Ghosts (Demo)" , "My Best Dress (Demo)" , "Donkey Kosh (Demo)" ,
           "Shake It Out (The Weeknd Remix)" , "Search And Destroy" , "Times Like These" , "Postcards From Italy (Demo)",
           "King (Poem Version)" , "How Big, How Blue, How Beautiful (Demo)" , "Cassandra (Poem Version)" ,
           "Try a Little Tenderness - MTV Unplugged, 2012" , "Paper Massacre" , "Silver Springs" , "Tear Out My Tongue / Ye Old Hope" ,
           "You’ve Got the Love (Jamie xx Rework)" , "Jackson - MTV Unplugged, 2012" , "Throwing Bricks" , "Don’t Tell Me" , "Stay With Me" ,
           "What the Water Gave Me (Demo)" , "My Love (Poem Version)" , "Flakes" , "Delilah (Demo)" , "Not Fade Away" ,
            "Bird Song Intro" , "Dog Days Are Over (Yeasayer Remix)" , "Cassandra (Acoustic)" , "Oh! Darling (Live At Abbey Road, UK / 2009)" ,
           "Only Love Can Break Your Heart (Live)" , "You’ve Got the Dirtee Love (Live at The Brit Awards / 2010)" ,
           "Free (Acoustic)",  "Morning Elvis (Acoustic)" , "My Love (Acoustic)" , "If I Had a Heart/Blinding" ,
           "Cosmic Love (Seven Lions Remix)" , "Delilah (Galantis Remix)" , "Shake It Out (Acoustic)" , "My Boy Builds Coffins (Acoustic)" ,
           "Heartlines (Acoustic)" , "Breaking Down (Acoustic)" , "Dog Days Are Over (Demo)", "Girl With One Eye - Bayou Percussion Version" ,
           "Free (The Blessed Madonna Remix)" , "My Love (MEDUZA Remix)" , "No Light, No Light - MTV Unplugged, 2012" ,
           "What Kind of Man (Nicholas Jaar Remix)" , "Never Let Me Go - MTV Unplugged, 2012" , "Only If For a Night - MTV Unplugged, 2012" ,
           "Drumming Song - MTV Unplugged, 2012" , "Cosmic Love - MTV Unplugged, 2012" ,
           "Strangeness & Charm - Live from Hammersmith Apollo / 2010" , "Swimming - Live from Hammersmith Apollo / 2010" ,
           "Breaking Down - MTV Unplugged, 2012" , "Hurricane Drunk (The Horrors Remix)" , "Shake It Out - MTV Unplugged, 2012" ,
           "Dog Days Are Over - MTV Unplugged, 2012" , "Shake It Out (Benny Benassi Remix)" ,
           "Rabbit Heart (Raise It Up) (Jamie T & Ben Bones Lionheart Mix)" , "Dog Days Are Over (Optimo Espacio Mix)" ,
           "What the Water Gave Me - MTV Unplugged, 2012" , "Girl with One Eye - iTunes Live: London Festival / 2010" ,
           "Heavy Intro - Live at The Wiltern / 2010" , "Hospital Beds - iTunes Live: London Festival / 2010" ,
           "Heavy In Your Arms (C-Berg Remix)" , "Drumming Song (Acoustic)" , "South London Forever (Acoustic)" ,
           "Rabbit Heart - Raise It Up (Acoustic)" , "My Boy Builds Coffins - iTunes Live: London Festival / 2010" ,
           "Hunger (Acoustic)" , "You’ve Got the Love (Live from Abbey Road)" , "Rabbit Heart (Raise It Up) - Live at the Wiltern / 2010" ,
           "Dog Days Are Over - iTunes Live: London Festival / 2010" , "Lover To Lover (Ceremonials Tour Version)" ,
           "Blinding - Live at the Wiltern / 2010" , "Strangeness & Charm - Live at the Wiltern / 2010" , "Patricia (Acoustic)" ,
           "Between Two Lungs - Live at the Wiltern / 2010" , "Ghosts - Live at the Wiltern / 2010" ,
           "You’ve Got the Love (Steve Pitron & Max Sanna Remix)" , "Drumming , London Festival / 2010" ,
           "You’ve Got the Love - Live at the Wiltern / 2010" , "Shake It Out (Benny Benassi Remix Edit)" , "Howl - Live at the Wiltern / 2010" ,
           "Heavy In Your Arms - Live at the Wiltern / 2010" , "An Offering (Rabbit Heart Demo)" , "Queen of Peace (Hot Chip Remix)" ,
           "You’ve Got the Love (Tom Middleton Remix)" , "Dog Days Are Over - Live at the Wiltern / 2010" ,
           "Drumming Song - Live at the Wiltern / 2010" , "Drumming Song (Jack Beats Remix)" , "Drumming Song (Boy 8-Bit Remix)" ,
           "Kiss With a Fist - Live at the Wiltern / 2010" , "Cosmic Love - Live at the Wiltern / 2010" ,
           "Rabbit Heart (Raise It Up) (Leo Zero Remix)" , "Hurricane Drunk - iTunes Live: London Festival / 2010" ,
           "My Boy Builds Coffins - Live at the Wiltern / 2010" , "Hurricane Drunk - Live at the Wiltern / 2010" ,
           "Blinding (traducción al español)" , "You’ve Got The Love (Mark Knight Remix)" , "My Love (MEDUZA Extended Remix)"
]

def get_raw_lyrics():
    genius = lyricsgenius.Genius('genius_client_access_token')
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

def handler():
    auth = tweepy.OAuth1UserHandler(
        CONSUMER_API_KEY,
        CONSUMER_API_SECRET_KEY
    )
    auth.set_access_token(
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)
    lyrics, song = get_raw_lyrics()
    tweet = get_tweet_from(lyrics)
    status = api.update_status(tweet)
    interval = 60 * 60 * 1
    time.sleep(interval)

    return tweet

if __name__ == "__main__":
     handler()
