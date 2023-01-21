"""
This file implements the different example models of wavelet modifications
seen in Table 1 of the paper.
"""
from Sound import Sound
import pywt

# Model : Scales the approx coefs linearly {{{
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
# }}}

# Model : Scales the details coefs linearly {{{
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
# }}}

# Model : linearly Scale wavelet filters
def linear_interpolation(x1, x2, y1, y2, x):
    return ( (y2 -y1)/(x2 - x1) )*( x - x1) + y1

def linear_down(array):
    half_array = [0]*(len(array)//2)
    for i in range( len(array)//2):
        half_array[i] = (array[2*i] + array[2*i +1])/2
    return half_array

def linear_up(array):
    """
        Given array is supposed to be of even size
    """
    a_length = len(array)
    twice_array = array
    for i in range(a_length//2):
        if i < a_length//2 -1:
            twice_array.insert(2*i+1, linear_interpolation(0, 1, twice_array[2*i], twice_array[2*i+1], .5))
        else:
            twice_array.insert(2*i+1, linear_interpolation(0, 1, twice_array[2*i], twice_array[2*i+1], .25))
            
    twice_array = twice_array[::-1]
    for i in range(a_length//2):
        if i < a_length//2 -1:
            twice_array.insert(2*i+1, linear_interpolation(0, 1, twice_array[2*i], twice_array[2*i+1], .5))
        else:
            twice_array.insert(2*i+1, linear_interpolation(0, 1, twice_array[2*i], twice_array[2*i+1], .25))
    twice_array = twice_array[::-1]
    return twice_array

def linScale_WavFilters(sound, scaleDown=True, wavelet_name):
    wavelet = pywt.Wavelet(wavelet_name)
    filterBank = wavelet.filter_bank
    scaled_filterBank = []
    if scaleDown:
        for filters in filterBank:
            scaled_filterBank.append( linear_down(filters) )
    else:
        for filters in filterBank:
            scaled_filterBank.append( linear_up(filters) )


    # Wavelet creation
    scaledFilters_wav = pywt.Wavelet('test', scaled_filterBank)

    # taking the discrete wavelet transform of the base rain sound
    dwt_baseSound = pywt.dwt(wavelet=wavelet, data=base_rain._array)
    # reconstruct it with the modified wavelet
    new_baseSound = Sound.from_array(pywt.idwt(*dwt_baseSound, wavelet=new_wav))
    return new_baseSound

    
# TODO Implement Filter points modifications
