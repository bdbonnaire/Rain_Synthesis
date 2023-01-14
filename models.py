"""
This file implements the different example models of wavelet modifications
seen in Table 1 of the paper.
"""
from Sound import Sound
import pywt

def scaleApprox_DWTCoef(sound, factor=2, wavelet='db4', level_dwt=5, play=False):

    dwt_base_sound = pywt.wavedec(sound._array, wavelet=wavelet, level=level_dwt)

    # pywt outputs a list if the following way : An Dn-1 Dn-2 ...
    # where An is the approximation coef and Dk are the details coef.
    dwt_base_sound[0] *= factor
    out_array = pywt.waverec(dwt_base_sound, wavelet=wavelet)
    modified_sound = Sound.from_array(out_array)
    if play:
        modified_sound.play()

    return modified_sound

def scaleDetails_DWTCoef(sound, factor=2, wavelet='db4', level_dwt=5, level_details=1, play=False):

    # tests the validity of details_level
    if details_level >= level_dwt:
        raise AttributeError("The given details level do not concord with the given dwt level.\n We must have level_details < level_dwt.")

    dwt_base_sound = pywt.wavedec(sound._array, wavelet=wavelet, level=level_dwt)

    # pywt outputs a list if the following way : An Dn-1 Dn-2 ...
    # where An is the approximation coef and Dk are the details coef.
    dwt_base_sound[-level_details] *= factor
    out_array = pywt.waverec(dwt_base_sound, wavelet=wavelet)
    modified_sound = Sound.from_array(out_array)
    if play:
        modified_sound.play()

    return modified_sound

# TODO Implement Filter points modifications
