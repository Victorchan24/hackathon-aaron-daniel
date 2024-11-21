import os

music_file = "game_music.wav"  # Or your actual file name

if os.path.exists(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
else:
    print(f"Error: {music_file} not found!")
