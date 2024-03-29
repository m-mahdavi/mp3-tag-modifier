##########################################################
# MP3 Tag Modifier
# Mohammad Mahdavi
# moh.mahdavi.l@gmail.com
# December 2015
##########################################################


##########################################################
import os
import mutagen.easyid3
##########################################################


##########################################################
MUSIC_FOLDER_PATH = "/mnt/c/Users/mmahdavi/Desktop/Me/Music"    # "/mnt/e/Music"   # "/media/mohammad/08CC2DB1CC2D99C8/Music"   #"D:/Music"   # "/mnt/e/Music"
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
			print(new_path)
			try:
				audio_file = mutagen.easyid3.EasyID3(new_path)
			except mutagen.id3.ID3NoHeaderError:
				audio_file = mutagen.File(new_path, easy=True)
				audio_file.add_tags()
			audio_file["artist"] = artist
			audio_file["album"] = album
			audio_file["title"] = ""
			audio_file["genre"] = ""
			audio_file["tracknumber"] = ""
			audio_file["albumartist"] = ""
			audio_file["date"] = ""
			audio_file.save()
##########################################################


##########################################################
if __name__ == "__main__":
	artist_list = os.listdir(MUSIC_FOLDER_PATH)
	for artist in artist_list:
		artist_folder_path = os.path.join(MUSIC_FOLDER_PATH, artist)
		if os.path.isdir(artist_folder_path):
			default_album = "Singles"
			dfsUpdate(artist_folder_path, artist, default_album)
##########################################################
