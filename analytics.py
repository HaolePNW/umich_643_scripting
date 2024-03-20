import pandas as pd

def create_tweet_count_df(tweets_df: pd.DataFrame, freq: str = 'M') -> pd.DataFrame:
    """
    Creates a DataFrame with the count of tweets aggregated by the specified frequency.
    
    Args:
    - tweets_df (pd.DataFrame): DataFrame containing tweets data.
    - freq (str): Frequency for resampling/aggregating data. Defaults to 'M' (monthly).
    
    Returns:
    - pd.DataFrame: A DataFrame with columns 'count' and 'created_at', representing
                    the number of tweets and the start time of each period, respectively.
    """
    if tweets_df.empty:
        return pd.DataFrame(columns=['count', 'created_at'])
    
    try:
        tweets_df = tweets_df.set_index(pd.DatetimeIndex(tweets_df['created_at']))
        t_count = tweets_df.resample(freq).size().reset_index(name='count')
        return t_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame(columns=['count', 'created_at'])  # Return an empty DataFrame in case of error

def create_favorite_avg_df(tweets_df: pd.DataFrame, freq: str = 'M') -> pd.DataFrame:
    """
    Creates a DataFrame with the average of favorites of tweets created each month.
    
    Args:
    - tweets_df (pd.DataFrame): DataFrame containing tweets data.
    - freq (str): Frequency for resampling/aggregating data. Defaults to 'M' (monthly).
    
    Returns:
    - pd.DataFrame: A DataFrame with columns 'favorite avg' and 'created_at', representing
                    the average favorites and the start time of each period, respectively.
    """
    if tweets_df.empty:
        return pd.DataFrame(columns=['favorite avg', 'created_at'])
    
    try:
        tweets_df = tweets_df.set_index(pd.DatetimeIndex(tweets_df['created_at']))
        t_fav = tweets_df.resample(freq)['favorite_count'].mean().reset_index(name='favorite avg')
        return t_fav
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame(columns=['favorite avg', 'created_at'])

def create_retweet_avg_df(tweets_df: pd.DataFrame, freq: str = 'M') -> pd.DataFrame:
    """
    Creates a DataFrame with the average of retweets of the tweets created each month.
    
    Args:
    - tweets_df (pd.DataFrame): DataFrame containing tweets data.
    - freq (str): Frequency for resampling/aggregating data. Defaults to 'M' (monthly).
    
    Returns:
    - pd.DataFrame: A DataFrame with columns 'retweet avg' and 'created_at', representing
                    the average retweets and the start time of each period, respectively.
    """
    if tweets_df.empty:
        return pd.DataFrame(columns=['retweet avg', 'created_at'])
    
    try:
        tweets_df = tweets_df.set_index(pd.DatetimeIndex(tweets_df['created_at']))
        t_rt = tweets_df.resample(freq)['retweet_count'].mean().reset_index(name='retweet avg')
        return t_rt
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame(columns=['retweet avg', 'created_at'])

# These functions are part of the analytics.py module, designed to perform different aggregations and computations
# on tweet data to extract insights such as tweet counts, average favorites, and average retweets per month.
