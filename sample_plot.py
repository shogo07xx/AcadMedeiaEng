# %%
from PIL import Image
import matplotlib.pyplot as plt
import os

# カレントディレクトリを移動
os.chdir(os.path.dirname(os.path.abspath(__file__)))

directory = "./data/"  # データディレクトリ
input_filename = "mario128.png" #データ名
img = Image.open(os.path.join(directory, input_filename)) # 画像を読み込む

# 入力画像を表示する
plt.subplot(2, 1, 1)
plt.imshow(img)
plt.axis("off")

plt.show()
# %%
