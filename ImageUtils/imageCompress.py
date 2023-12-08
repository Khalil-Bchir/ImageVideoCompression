from flask import render_template
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import requests


def compress_image(url, max_size):
    try:
        # Download the image from the URL
        response = requests.get(url)

        # Check if the response was successful
        response.raise_for_status()

        # Print additional information for debugging
        print(f"Downloaded Image URL: {url}")
        print(f"Downloaded Image Content-Type: {response.headers['content-type']}")

        # Check if the content is an image
        if not response.headers['content-type'].startswith('image'):
            raise UnidentifiedImageError("The provided URL does not contain a valid image.")

        original_image = Image.open(BytesIO(response.content))

        # Convert the image to WEBP format with quality adjustment
        compressed_image = BytesIO()
        original_image.save(compressed_image, format='WEBP', quality=85)  # You can adjust the quality value

        # Check if the compression was successful
        if compressed_image.getvalue() == b'':
            raise Exception("Image compression failed. The compressed image is empty.")

        # Get the dimensions of the compressed image directly from the original Image object
        compressed_dimensions = original_image.size

        # Log statements for debugging
        print(f"Original Size: {len(response.content)} bytes")
        print(f"Compressed Size: {compressed_image.getbuffer().nbytes} bytes")

        # Log additional information for debugging
        print(f"Original Dimensions: {original_image.size}")
        print(f"Compressed Dimensions: {compressed_dimensions}")
        print(f"Original Format: {original_image.format}")

        # Calculate compression stats
        stats = {
            'original_size': len(response.content),
            'compressed_size': compressed_image.getbuffer().nbytes,
            'original_dimensions': original_image.size,
            'compressed_dimensions': compressed_dimensions,
            'original_format': original_image.format,
            'compressed_format': 'WEBP'
        }

        return compressed_image, stats

    except requests.exceptions.RequestException as e:
        error_message = f"Error: {e}. There was an issue with the request to the provided URL."
        return None, {'error_message': error_message, 'success': False}
    except UnidentifiedImageError as e:
        error_message = f"Error: {e}. The provided URL does not contain a valid image."
        return None, {'error_message': error_message, 'success': False}
    except Exception as e:
        error_message = f"Error: {e}. An unexpected error occurred during image compression."
        return None, {'error_message': error_message, 'success': False}
