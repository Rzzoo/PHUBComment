
from PIL import Image, ImageFont, ImageDraw, ImageOps

phub = Image.open('phubtemplate.jpg')
avaa = Image.open(f'avatar.jpg')
avaa = avaa.resize((70, 70))
phub.paste(avaa, (29, 338))
phub.save('result.jpg')
res = Image.open('result.jpg')
type = ImageDraw.Draw(res)
font = ImageFont.truetype("helvetica.ttf", 30)
type.text((114, 357),'Your Name Here',(245,161,48,255),font=font)
res.save("result.jpg")
res = Image.open('result.jpg')
type = ImageDraw.Draw(res)
font = ImageFont.truetype("helvetica.ttf", 30)
type.text((32, 443),'Your Comment Here',(255,255,255,255),font=font)
res.save("result.jpg")
print('Done!')
