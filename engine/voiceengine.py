from gtts import gTTS
from pydub import AudioSegment
import eel
from www import *
import time 
from pydub.playback import play

import io
def say(text, speed=1.35):
    # text = str(text)
    # eel.DisplayMessage(text)
    # Initialize gTTS object with the given text and language
    tts = gTTS(text, lang='en', slow=False)  # Set 'slow' to False to use the default speed

    # Save the speech to a BytesIO object instead of a file
    with io.BytesIO() as audio_file:
        tts.write_to_fp(audio_file)  # Write the speech to the BytesIO object
        audio_file.seek(0)  # Move to the beginning of the BytesIO object

        # Load the audio data into a pydub AudioSegment
        audio = AudioSegment.from_file(audio_file, format="mp3")

        # Change playback speed
        new_frame_rate = int(audio.frame_rate * speed)
        altered_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_frame_rate})
        altered_audio = altered_audio.set_frame_rate(audio.frame_rate)  # Ensure compatibility

        # Play the audio
        play(altered_audio)

# # Example usage
# if __name__ == '__main__':
#     say("Hello, how can I assist you today?")  # Adjust speed (1.0 is normal speed)
