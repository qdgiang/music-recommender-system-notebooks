import pandas as pd

# define a function that return the song name for the given id
def whats_that_song(id: str, df: pd.DataFrame) -> str:
    return df.loc[id, 'song_id']

def show_user_history(user_id: str, df: pd.DataFrame) -> None:
    """Print the song history for the given user id."""
    return df[df.user_id == user_id]

def show_most_listend_artist(df: pd.DataFrame) -> None:
    """Show the list of most listened artists"""
    print('Most listened artists by user:')
    print(df.artist_name.value_counts())