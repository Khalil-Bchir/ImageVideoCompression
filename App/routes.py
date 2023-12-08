import base64
from urllib.parse import unquote

from flask import render_template

from flask import Flask, request, jsonify

from ImageUtils.imageCompress import compress_image

app = Flask(__name__)


@app.route('/compress', methods=['POST'])
def compress_image_api():
    try:
        # Get image URL from the request
        image_url = request.json['image_url']

        # Decode the URL
        decoded_image_url = unquote(image_url)

        # Print the decoded URL for debugging
        print(f"Decoded Image URL: {decoded_image_url}")

        # Set maximum size for compression (adjust as needed)
        max_size = 1024 * 1024  # 1 MB

        # Compress the image
        compressed_image, compression_stats = compress_image(decoded_image_url, max_size)

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


@app.route('/')
def index():
    return render_template('index.html')
