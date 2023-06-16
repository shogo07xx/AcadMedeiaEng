# %%
# %matplotlib inline
import librosa
import librosa.display
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import os


# カレントディレクトリを移動
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# オーディオファイルを読み込む
directory = "./data/"
input_filename = "babbling_brook.mp3"
# input_filename = "vocaloid_sample.mp3"
# input_filename = "nightcore_sample.mp3"
audio_path = os.path.join(directory, input_filename)
y, sr = librosa.load(audio_path)

# 時間軸を計算（単位：秒）
time = np.arange(0, len(y)) / sr

# 周波数成分に分離し、スペクトログラムを計算
hop_length = int(sr/100)  # Set hop_length to match time resolution of waveform
y_harm, y_perc = librosa.effects.hpss(y)
spectrogram = librosa.amplitude_to_db(librosa.magphase(librosa.stft(y_harm, hop_length=hop_length))[0], ref=np.max)

# 波形とスペクトログラムをプロット
fig, axs = plt.subplots(2, 1, sharex=True, figsize=(14, 5))
axs[0].plot(time, y)
axs[0].set_ylabel("Amplitude")
axs[0].set_title("Waveform")
cmap = cm.get_cmap('inferno')
img = librosa.display.specshow(spectrogram, x_axis='time', y_axis='log', sr=sr, hop_length=hop_length, ax=axs[1], cmap=cmap)
axs[1].set_xlabel("Time (s)")
axs[1].set_ylabel("Frequency (Hz)")
axs[1].set_title("Spectrogram")

# カラーバーを追加
plt.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.9, 0.3, 0.02, 0.4])
plt.colorbar(img, cax=cbar_ax, format="%+2.0f dB")

# スペクトログラムの高さを取得
spectrogram_height = axs[1].get_position().height

# カラーバーの高さをスペクトログラムの高さに合わせる
cbar_ax.set_position([0.92, axs[1].get_position().y0, 0.02, spectrogram_height])

plt.subplots_adjust(hspace=0.5)
plt.show()

import IPython.display
IPython.display.Audio(audio_path)
# %%
