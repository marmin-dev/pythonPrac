from PIL import Image

mask = Image.open('mask.png')
word = Image.open('word_matrix.png')

print(word.size)
print(mask.size)

mask = mask.resize((1015,559))
print(mask.size)
mask.putalpha(200)
# Image.paste(im, box=None, mask=None)[source]
# word.paste(mask, (0,0),mask)
image1 = Image.blend(word,mask,0.5)
image1.show()