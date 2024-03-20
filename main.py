# main.py

import loaders
import analytics
import visualizations

def main():
    # Step 1: Load tweet data
    directory_path = '.\assets'
    tweets_df = loaders.create_tweet_df(directory_path)
    
    if tweets_df.empty:
        print("No tweets loaded. Please check your data directory path.")
        return
    
    # Step 2: Perform analysis
    t_count = analytics.create_tweet_count_df(tweets_df)
    t_fav = analytics.create_favorite_avg_df(tweets_df)
    t_rt = analytics.create_retweet_avg_df(tweets_df)
    
    # Step 3: Generate and display visualization
    combined_chart = visualizations.create_tweet_sum_viz(t_count, t_rt, t_fav)
    combined_chart.display()  

if __name__ == "__main__":
    main()
