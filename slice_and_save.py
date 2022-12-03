from pydub import AudioSegment
from tqdm import tqdm

sound = AudioSegment.from_file("./Sounds/Rain/heavy_rain.m4a", format="m4a")

# Slice the audio in N clips of size `size`
N = 100
size = 10 * 1000

for i in tqdm(range(N)):
    sound[i*size : (i+1)*size].export("./Sounds/Rain/heavy_rain_{:02d}.wav".format(i), format="wav")
