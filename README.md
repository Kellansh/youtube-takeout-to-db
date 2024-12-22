What I want:
A database of all my YouTube playlists, containing info for each video:
- Video ID
- Add time
- Title
- Uploader name
- Upload date
- Thumbnail image
A command I can run that will update the database:
1. Find YouTube CSVs in a Google Takeout folder
2. Check which playlists are new or updated
3. If a playlist was added, 
    3a. Fill in all video details
    3b. Add it to the DB
4. If a playlist was updated,
    4a. Look up details of each video ID that has been added or deleted
    4b. If a video was added, add its info to the playlist's table
    4c. If a video was "deleted", check looking up the video ID now returns an error (in which case it was likely deleted by YouTube, not me). If there's no error, mark the video on the playlist as deleted by me

To do:
- solve downloading thumbnails
- initialize db
- decide whether to use prisma/other
- start sql command section