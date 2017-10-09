##########################################################
# MP3 Tag Modifier
# Mohammad Mahdavi
# moh.mahdavi.l@gmail.com
# December 2015
# All Rights Reserved
##########################################################


##########################################################
import os
import mutagen.easyid3
##########################################################


##########################################################
MUSIC_FOLDER_PATH = "D:/Music"
##########################################################


##########################################################
def dfsUpdate(path, artist, album):
	file_list = os.listdir(path)
	for a_file in file_list:
		new_path = os.path.join(path, a_file)
		if os.path.isdir(new_path):
			album = a_file
			dfsUpdate(new_path, artist, album)
		elif a_file.lower().endswith(".mp3"):
			print new_path
			audio_file = mutagen.easyid3.EasyID3(new_path)
			audio_file["artist"] = artist.decode("utf-8")
			audio_file["album"] = album.decode("utf-8")
			# audio_file["title"] = ""
			# audio_file["date"] = 2000
			audio_file.save()
##########################################################


##########################################################
if __name__ == "__main__":
	artist_list = os.listdir(MUSIC_FOLDER_PATH)
	for artist in artist_list:
		artist_folder_path = os.path.join(MUSIC_FOLDER_PATH, artist)
		default_album = "Single"
		dfsUpdate(artist_folder_path, artist, default_album)
##########################################################
