
# Media Compression App

This is a simple Flask application for compressing videos and images. Users can choose to compress either a video or an image by providing the respective URL. The application uses ffmpeg for video compression and other libraries for image compression.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python app.py
   ```

   The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. Open the application in your web browser.

2. Choose whether you want to compress a video or an image.

3. For Video Compression:
   - Enter the video URL in the provided input field.
   - Click the "Compress Video" button.
   - After compression, a downloadable link to the compressed video will be provided.

4. For Image Compression:
   - Enter the image URL in the provided input field.
   - Click the "Compress Image" button.
   - After compression, a downloadable link to the compressed image will be provided.

## Dependencies

- Flask
- ffmpeg (Make sure ffmpeg is installed on your system. You can download it from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)).
- Other image compression libraries (if applicable).

## Contributing

If you'd like to contribute to the project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This version focuses on the essential setup and usage instructions for users, without explicitly mentioning virtual environment setup. Users familiar with Python development will generally understand the importance of virtual environments, but you can always provide additional instructions as needed.
