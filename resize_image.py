from PIL import Image
import matplotlib.pyplot as plt
import os

directory = "./data/"  # 画像ディレクトリ
input_filename = "mario128.png"
output_filename = "mario_resized.png"  # リサイズ画像のファイル名

def resize_image(img, size = (64, 64)):
    # 画像をRGBAモードに変換
    img = img.convert("RGBA")
    
    # 元画像のサイズを取得
    width, height = img.size
    
    # リサイズ後の画像サイズを計算
    new_size = (width // 2, height // 2)
    
    # リサイズ後の画像を格納する新しいImageオブジェクトを作成
    resized_img = Image.new("RGBA", new_size)
    
    """
    # forループを使ってリサイズ
    for i in range(new_size[1]):
        for j in range(new_size[0]):
            resized_img.putpixel((j, i), img.getpixel((j * 2, i * 2)))
    """

    # リサイズのためのスケールファクターを計算
    x_scale = width / size[0]
    y_scale = height / size[1]
    
    # 最近傍補間によりリサイズ

    # この部分を実装


    return resized_img

# 画像を読み込む
img = Image.open(os.path.join(directory, input_filename))

# 画像をリサイズする
resized_img = resize_image(img)

# リサイズ画像を保存する
resized_img.save(os.path.join(directory, output_filename))

# 入力画像を表示する
plt.figure(figsize=(img.size[0] / plt.rcParams["figure.dpi"], img.size[1] / plt.rcParams["figure.dpi"]))
plt.imshow(img)
plt.axis("off")
plt.title("Input Image")
plt.show()

# リサイズ後の画像を表示する
plt.figure(figsize=(resized_img.size[0] / plt.rcParams["figure.dpi"], resized_img.size[1] / plt.rcParams["figure.dpi"]))
plt.imshow(resized_img)
plt.axis("off")
plt.title("Resized Image")
plt.show()
