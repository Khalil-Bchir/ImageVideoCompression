import base64

from flask import Flask, request, jsonify
from flask import render_template, send_file

from ImageUtils.imageCompress import compress_image
from ImageUtils.videoCompression import compress_video

app = Flask(__name__)


@app.route('/compress_image', methods=['POST'])
def compress_image_api():
    try:
        # Get image URL and compression format from the request
        image_url = request.json['image_url']

        # Set maximum size for compression (adjust as needed)
        max_size = 1024 * 1024  # 1 MB

        # Compress the image
        compressed_image, compression_stats = compress_image(image_url, max_size)

        # Convert compressed image to base64
        compressed_image_base64 = base64.b64encode(compressed_image.getvalue()).decode('utf-8')

        # Prepare response
        response_data = {
            'success': True,
            'compressed_image': compressed_image_base64,
            'compression_stats': compression_stats
        }

        return jsonify(response_data)

    except Exception as e:
        # Handle errors
        error_response = {
            'success': False,
            'error_message': str(e)
        }
        return jsonify(error_response)


@app.route('/compress_video', methods=['POST'])
def compress_video_api():
    data = request.get_json()

    # Check if the 'video_url' parameter is provided in the request
    if 'video_url' not in data:
        return jsonify({'error': 'Missing video_url parameter'}), 400

    video_url = data['video_url']

    print(f"Received video_url: {video_url}")

    try:
        compressed_video = compress_video(video_url)
        print("Video compressed successfully")
        return send_file(compressed_video, as_attachment=True, download_name='compressed_video.mp4'), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/image')
def compressimage():
    return render_template('image.html')

@app.route('/video')
def compressvideo():
    return render_template('video.html')
