""" 
Gist:

For each playlist in folder:

1. Take in playlist

2. Add columns: title, author name, thumbnail name, freeform notes

3. For each row/video ID:

3a. Grab info from noembed

3b. Download image from thumbnail URL

3c. Append title and author name

4. Format playlist to import if needed

Then backup database, then update database to match

"""

import pandas as pd
import numpy as np
import requests

df = pd.read_csv("example_playlist.csv", header=0)

def get_noembed_info(row, attribute):
    res = requests.get('https://noembed.com/embed?url=https://www.youtube.com/watch?v='+row['Video ID']).json()

    if 'error' in res:
        print('Error for row',row.index,'with video ID',row['Video ID'])
        print('Output from noembed:',res['error'])
        return res['error'], res['error']
    else:
        return res[attribute]

df['Title'] = df.apply(get_noembed_info, attribute=('title'), axis=1)
df['Author_Name'] = df.apply(get_noembed_info, attribute=('author_name'), axis=1)

# todo: ability to optionally download each thumbnail (with video ID as image name)

print(df.head())