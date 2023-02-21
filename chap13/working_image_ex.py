from PIL import Image
duhan = Image.open('kimduhan.jpg')
print(type(duhan))
# show the picture
# duhan.show()
# find pixel of image
print(duhan.size)
# 형식에 대한 구체적인 정보가 필요할 경우
print(duhan.format_description)
# crop method : 이미지의 한 부분 가져오기 실제 저장 가능
# box 매개변수는 좌측,상단,우측 하단 픽셀의 좌표 4가지를 정의하는 튜플
# 좌측 맨 상단 0.0 좌표



x = 300
y = 150

w = 600
h = 400

face = duhan.crop((x,y,w,h))
# paste image on image
duhan.paste(im=face,box=(100,100))
# duhan.show()
# resize the image


# 투명도 RGBA 0~255 알파값이 0 이면 투명해진다
duhan.putalpha(90)
duhan.show()
# 저장하기
duhan.save("duhanuyee.png")