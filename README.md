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
   git clone https://github.com/A-D-E-L-M-A-H-M-O-U-D/Whisper-Video-Audio-Transcriber.git
   ```
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
    ```
    pip install datetime
    ```
3. install FFmpeg for audio extraction from video files

- Download FFmpeg from [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z) for windows

- Extract all ffmpeg folder in your C drive (`C:\`)

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

- If you are need running on your GPU (Graphics card), you can remove the fp16=False option to enable half-precision floating point (FP16) for faster performance on supported hardware. Simply remove this option from code :

    ```result = model.transcribe(file_name) ```
- fp16 for transcription on GPU
- fp32 or fp16=False for transcription on cpu (processor)
## Available models

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and inference speed relative to the large model; actual speed may vary depending on many factors including the available hardware.

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

## Troubleshooting
- If you encounter any issues, ensure that your Python environment is set up correctly with the required libraries.

- Make sure FFmpeg is installed for audio extraction from video files.
