import json
d = json.load(open("MyData/Streaming_History_Audio_2020-2023_0.json", "r"))

names = []

#if i ever work on this more I'll do a dict that adds up how often ive listened to each and use that data in the game so that i dont come across obscure songs
for x in d:
    if x['master_metadata_track_name'] and x['master_metadata_album_artist_name']:
        if [x['master_metadata_track_name'], x['master_metadata_album_artist_name']] not in names:
            names.append([x['master_metadata_track_name'], x['master_metadata_album_artist_name']])

print(names)
print(len(names))

with open("names", "w+") as f:
    f.write("\n".join([f"{name[0]}|||{name[1]}" for name in names]))
