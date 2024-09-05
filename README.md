# Video to Audio Transcription using Whisper

This project allows you to convert a video file to audio, and then transcribe the audio into text using OpenAI's Whisper model. The transcription can be saved in SRT or VTT format.

## Features
- Convert video to audio.
- Transcribe audio using Whisper's `tiny` model.
- Save transcriptions as SRT or VTT files.

## Prerequisites
- Python 3.7 or higher
- FFmpeg
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/adel1046/Whisper-Video-Audio-Transcriber.git
   cd Whisper-Video-Audio-Transcriber
2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```
- Alternatively, you can install them manually:

    ```
    pip install whisper
    ```
    ```
    pip install moviepy
    ```
    ```
    pip install tkinter
    ```
3. install FFmpeg or audio extraction from video files

- Download FFmpeg from [here](https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-2024-09-02-git-3f9ca51015-full_build.7z)

- Extract all in ```C:\```

- open it and open bin folder 

- copy path of bin folder 

- In the Windows search bar, type Settings to open your Windows Settings.

- Search for Edit environment variables

- In your User variables, select the Path variable and then select Edit.

- Select New and add ``` path ```

## Running the Application
- Select a video or audio file

- Enter the base name for your output file (without extension)

- Choose the desired output format: SRT, VTT, or both

## Notes

- The tiny Whisper model is used by default, but you can modify the script to load a anthoer model like ( large , base , small , medium )

- The application supports video formats: .mp4, .wmv, .mov, .mkv, .h.264 and audio formats: .mp3, .wav

## Troubleshooting
- If you encounter any issues, ensure that your Python environment is set up correctly with the required libraries.

- Make sure FFmpeg is installed for audio extraction from video files.# Whisper-Video-Audio-Transcriber
