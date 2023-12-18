from moviepy.editor import VideoFileClip

def convert_video_to_audio(path):
    try:
        # Check if the POST request has a file part
        # if 'file' not in request.files:
        #     return jsonify({'error': 'No file part'})
        #
        # file = request.files['file']
        #
        # # Check if the file is empty
        # if file.filename == '':
        #     return jsonify({'error': 'No selected file'})

        # Check if the file is a video
        # if file.mimetype.startswith('video'):
        #     # Save the video file
        #     video_path = 'ayat.mp4'
        #     file.save(video_path)

            # Convert video to audio using moviepy
        video_clip = VideoFileClip(path)
        audio_path = 'converted_audio.wav'
        video_clip.audio.write_audiofile(audio_path)
        video_clip.close()
        return jsonify({'success': 'Video converted to audio', 'audio_path': audio_path})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
