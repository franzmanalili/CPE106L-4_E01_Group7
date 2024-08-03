import sqlite3
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://godleano:1234@softwaredesignlab.ik5jehq.mongodb.net/')
db = client['Lab5']

# Define the collections
artists_collection = db['Artists']
albums_collection = db['Albums']
tracks_collection = db['Tracks']

# Connect to SQLite database
sqlite_conn = sqlite3.connect('chinook.db')
cursor = sqlite_conn.cursor()

# Read and insert artists data
cursor.execute("SELECT ArtistId, Name FROM artists")
artists_data = [{"_id": row[0], "Name": row[1]} for row in cursor.fetchall()]
artists_collection.insert_many(artists_data)
print("Artists data inserted successfully")

# Read and insert albums data
cursor.execute("SELECT AlbumId, Title, ArtistId FROM albums")
albums_data = [{"_id": row[0], "Title": row[1], "ArtistId": row[2]} for row in cursor.fetchall()]
albums_collection.insert_many(albums_data)
print("Albums data inserted successfully")

# Read and insert tracks data
cursor.execute("""
SELECT TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice 
FROM tracks
""")
tracks_data = [{
    "_id": row[0],
    "Name": row[1],
    "AlbumId": row[2],
    "MediaTypeId": row[3],
    "GenreId": row[4],
    "Composer": row[5],
    "Milliseconds": row[6],
    "Bytes": row[7],
    "UnitPrice": row[8]
} for row in cursor.fetchall()]
tracks_collection.insert_many(tracks_data)
print("Tracks data inserted successfully")

# Close SQLite connection
sqlite_conn.close()

# Verify data insertion
print("\nArtists Collection:")
for artist in artists_collection.find():
    print(artist)

print("\nAlbums Collection:")
for album in albums_collection.find():
    print(album)

print("\nTracks Collection:")
for track in tracks_collection.find():
    print(track)




