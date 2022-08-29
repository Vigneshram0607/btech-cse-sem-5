import matplotlib.pyplot as plt
# %matplotlib inline

filename = '/Users/vigneshram/Desktop/MINI PROJECT/ML/UrbanSound8K/dog_bark.wav'


import IPython.display as ipd
import librosa
import librosa.display
plt.figure(figsize=(14,5))
data,sample_rate = librosa.load(filename)
librosa.display.waveshow(data, sr=sample_rate)
ipd.Audio(filename)
