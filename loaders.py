# loaders.py
import os
import json
import pandas as pd
import numpy as np

def create_tweet_df(directory_path: str = r'\Users\bdens\OneDrive\Personal\UMich\Social Media Analy 682\assets') -> pd.DataFrame:
    """
    Loads tweets from JSON files in a specified directory, formats them, and returns a pandas DataFrame.
    
    Args:
    - directory_path (str): Path to the directory containing tweet JSON files. Defaults to a specified path.
    
    Returns:
    - pd.DataFrame: A DataFrame containing details of the tweets.
    """
    tweet_data = []
    
    try:
        # Iterate over every file in the given directory
        for file_name in os.listdir(directory_path):
            # Construct the full path to the file
            file_path = os.path.join(directory_path, file_name)
            
            # Process only json files
            if os.path.isfile(file_path) and file_name.endswith('.json'):
                with open(file_path, 'r') as json_file:
                    tweets = json.load(json_file)

            for tweet in tweets:
                text_content = tweet.get('full_text') or tweet.get('text', '')
                created_at_datetime = pd.to_datetime(tweet['created_at'])
                created_at_np = np.datetime64(created_at_datetime)
                
                tweet_data.append({
                    'retweet_count': int(tweet['retweet_count']),
                    'created_at': created_at_np,
                    'text': text_content,
                    'favorited': tweet['favorited'],
                    'retweeted': tweet['retweeted'],
                    'lang': tweet['lang'],
                    'favorite_count': int(tweet['favorite_count'])
                })

        tweets_df = pd.DataFrame(tweet_data)
        return tweets_df
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error
