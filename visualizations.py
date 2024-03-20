# visualizations.py
import altair as alt

def create_tweet_sum_viz(t_count, t_rt, t_fav):
    """
    Generates a combined horizontal bar chart visualization for tweet counts, retweet averages,
    and favorite averages over time.
    
    Args:
    - t_count (pd.DataFrame): DataFrame with tweet counts and timestamps.
    - t_rt (pd.DataFrame): DataFrame with average retweets and timestamps.
    - t_fav (pd.DataFrame): DataFrame with average favorites and timestamps.
    
    Returns:
    - alt.HConcatChart: An Altair chart object that can be displayed in Jupyter notebooks or saved as an image.
    """
    def create_bar_chart(df, metric_name):
        return alt.Chart(df).mark_bar().encode(
            x='created_at:T',
            y=f'{metric_name}:Q',
            tooltip=['created_at:T', f'{metric_name}:Q']
        ).properties(
            width=200,  # Width of each chart
            height=150  # Height of each chart
        )
    
    chart_count = create_bar_chart(t_count, 'count')
    chart_rt = create_bar_chart(t_rt, 'retweet avg')
    chart_fav = create_bar_chart(t_fav, 'favorite avg')
    
    combined_chart = alt.hconcat(chart_count, chart_rt, chart_fav, spacing=30) 
    return combined_chart
