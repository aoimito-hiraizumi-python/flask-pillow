from PIL import Image
# PIL をベースに作ったライブラリ pillow のこと

img = Image.open("images/cat.png")
#Imageのファイルを読み込む

frame = Image.open("images/frame.png")

resized_frame = frame.resize((img.width, img.height))
#frameの画像のサイズをネコの画像のサイズに合わせる

img.paste(resized_frame, (0, 0), resized_frame)
# 画像をくっつける (くっつける画像、座標、)

img.save("images/out.png")
# 新しく作った画像を保存する

img.show()
