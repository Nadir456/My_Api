from moviepy.editor import VideoFileClip

def convert_video_to_audio(video_path, audio_path):
    try:
        # Load the video clip
        video_clip = VideoFileClip(video_path)

        # Extract the audio from the video
        audio_clip = video_clip.audio

        # Save the audio file
        audio_clip.write_audiofile(audio_path)

        # Close the video and audio clips
        video_clip.close()
        audio_clip.close()

        print(f'Success: Video converted to audio. Audio saved at {audio_path}')

    except Exception as e:
        print(f'Error: {str(e)}')

# Specify the path to your video file and the desired audio file output path
video_path = 'ayat.mp4'  # Replace with the actual path to your video file
audio_path = 'con_ayat.wav'  # Replace with the desired path for the audio output file

# Convert the video to audio
convert_video_to_audio(video_path, audio_path)
