import whisper
import warnings
from whisper.utils import WriteSRT, WriteVTT
from tkinter import filedialog, Tk
import moviepy.editor
from datetime import datetime
import os

def video_to_audio(video_name):
    print("_" * 26 + "CONVERT" + "_" * 26)
    print("Converting video to audio...")

    try:
        video = moviepy.editor.VideoFileClip(video_name)
        print("Video uploaded...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        audio_file_name = f"audio_{timestamp}.mp3"
        audio = video.audio
        audio.write_audiofile(audio_file_name)
        print(f"Audio file name: {audio_file_name}")

        # Display audio file size
        with open(audio_file_name, "rb") as f:
            audio_size = len(f.read())
            print(f"Audio file size: {(audio_size) * 0.000001:.2f}MB")
        print("Successful conversion")
        
        return audio_file_name
    except Exception as e:
        print(f"An error occurred during video-to-audio conversion: {e}")
        return None

def main():
    # Initialize Tkinter root window (hidden)
    root = Tk()
    root.withdraw()

    # Ask user to select a file
    file_name = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Video Files", "*.mp4;*.wmv;*.mov;*.mkv;*.H.264;*.mp3;*.wav")]
    )
    
    if not file_name:
        print("No file selected. Exiting.")
        return

    # Check if the selected file is a video or audio
    file_extension = os.path.splitext(file_name)[1].lower()
    if file_extension in [".mp4", ".wmv", ".mov", ".mkv", ".h.264"]:
        file_name = video_to_audio(file_name)
        if not file_name:
            return
    elif file_extension in [".mp3", ".wav"]:
        print(f"File: {file_name}")
        print("Selected audio file.")
    else:
        print("Invalid file type selected. Exiting.")
        return

    # Suppress warnings
    warnings.filterwarnings("ignore", category=UserWarning, message="FP16 is not supported on CPU; using FP32 instead")
    warnings.simplefilter(action='ignore', category=FutureWarning)

    # Load the model
    print("Loading model...")
    model = whisper.load_model("tiny")
    print("Model loaded successfully.")

    # Transcribe audio to text
    print("Starting transcription...")
    try:
        result = model.transcribe(file_name, fp16=False) #If you are need running on your GPU (Graphics card), you can remove the fp16=False option for faster performance
        print("Transcription completed.")
        print("Transcription completed.")
    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        return
    
    while True:
        # Ask user for the base name for the output file
        base_filename = input("Enter the base name for the output file (without extension): ").strip()
        if base_filename:
            break
        print("Invalid input. Please enter a name for your file.")

    while True:
        # Ask user for file format preference
        choice = input("Which file format would you like to save? (Enter 'srt', 'vtt', or 'both'): ").strip().lower()
        if choice in ["srt", "vtt", "both"]:
            break
        print("Invalid choice. Please enter 'srt', 'vtt', or 'both'.")
    # Define output directory
    output_dir = os.getcwd()

    # Save SRT file if requested
    if choice in ["srt", "both"]:
        srt_filename = f"{base_filename}.srt"
        print(f"Saving results as SRT file to {output_dir}/{srt_filename}")
        srt_writer = WriteSRT(output_dir)
        try:
            with open(f"{output_dir}/{srt_filename}", "w", encoding="utf-8") as srt_file:
                srt_writer.write_result(result, srt_file)
            print(f"SRT file saved successfully as {srt_filename}")
        except Exception as e:
            print(f"An error occurred while saving SRT file: {e}")

    # Save VTT file if requested
    if choice in ["vtt", "both"]:
        try:
            vtt_filename = f"{base_filename}.vtt"
            print(f"Saving results as VTT file to {output_dir}/{vtt_filename}")
            vtt_writer = WriteVTT(output_dir)
            try:
                with open(f"{output_dir}/{vtt_filename}", "w", encoding="utf-8") as vtt_file:
                    vtt_writer.write_result(result, vtt_file)
                print(f"VTT file saved successfully as {vtt_filename}")
            except Exception as e:
                print(f"An error occurred while saving VTT file: {e}")
        except ImportError:
            print("WriteVTT class not found. VTT file was not created.")

    #clean up temporary files
    if os.path.exists(file_name):
        os.remove(file_name)

if __name__ == "__main__":
    main()
