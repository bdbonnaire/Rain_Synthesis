import numpy as np
import simpleaudio
# For loading and decoding of audio files
from pydub import AudioSegment
# allows playback
from pydub.playback import play
import array

class Sound() :
    """
        A wrapper class around pydub representing a sound with methods for convenience.
        Only accepted format for now is wav.
    """
    def __init__(self, file):
        # loading the file into a pydub object
        try:
            self._sound = AudioSegment.from_file(file, format='wav')
        except FileNotFoundError:
            print("Wrong filename, please check that the file exists.")
            raise FileNotFoundError
            # TODO : add other possible exceptions

        # gets the np array of samples from the pydub object
        self._array = np.array(self._sound.get_array_of_samples())

    @classmethod
    def from_array(cls, array):
        """
            constructor to create a sound object from a numpy array.
        """
        import io
        import scipy.io.wavfile

        wav_io = io.BytesIO()
        scipy.io.wavfile.write(wav_io, 16000, array)
        wav_io.seek(0)
        return cls(wav_io)

    def get_array(self):
        return self._array

    def play(self):
        play(self._sound)

    def update_sound_from_array(self):
        """
            This method updates the internal pydub sound object from the attribute _array. 
            This is useful if computations have been made on the array and the sound needs to be played back.
        """
        self._sound = self._sound._spawn(array.array(self._sound.array_type, self._array.astype(np.int16)))

    def reinitialize_array(self):
        """
            Reinitialize _array from _sound.
        """

        self._array = np.array(self._sound.get_array_of_samples())
