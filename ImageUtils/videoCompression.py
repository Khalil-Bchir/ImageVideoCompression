import io
import ffmpeg


def compress_video(video_url):
    # In-memory file
    output_file = io.BytesIO()

    # Using ffmpeg.input() to read from the URL
    input_stream = ffmpeg.input(video_url)

    # Using ffmpeg.output() to specify the output options
    output_stream = ffmpeg.output(input_stream, output_file, c='libx264', crf=20, preset='medium', tune='film',
                                  pix_fmt='yuv420p')

    # Running the ffmpeg command
    ffmpeg.run(output_stream)

    # Returning the in-memory file
    output_file.seek(0)
    return output_file
