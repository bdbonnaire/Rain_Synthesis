import numpy as np
import pywt
import simpleaudio
from pydub import AudioSegment

# Original sound
sound = AudioSegment.from_file("./Sounds/Rain/heavy_rain_00.wav", format="wav")
# a ndarray containning the sound
sound_array = np.array(AudioSegment.from_file("./Sounds/Rain/heavy_rain_00.wav", format="wav").get_array_of_samples())

cA, cD = pywt.dwt(sound_array, 'db2')
new_array = pywt.idwt(cA, cD, 'db2')
 h<F7>
import array
new_sound = sound._spawn(array.array(sound.array_type, new_array.astype(np.int16)))

from pydub.playback import play
print('Playing original sound')
input('press Enter to continue...')
play(sound)

print('Playing wavelet transformed sound')
input('press Enter to continue...')
play(new_sound)
#play_obj = simpleaudio.play_buffer(new_array, 2,2, 44100)
#play_obj.wait_done()
