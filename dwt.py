from Sound import Sound
import pywt
import matplotlib.pyplot as plt 
# Original sound
sound = Sound("./Sounds/Rain/heavy_rain_00_mono.wav")
# a ndarray containning the sound
sound_array = sound.get_array()
cA, cD = pywt.dwt(sound_array, 'db2')
new_array = pywt.idwt(cA, cD, 'db2')
new_sound = Sound.from_array(new_array)

print('Playing original sound')
input('press Enter to continue...')
print(sound.duration_seconds, sound.frame_rate)
sound.play()

print('Playing wavelet transformed sound')
input('press Enter to continue...')

print(new_sound.duration_seconds, new_sound.frame_rate)
new_sound.play()
