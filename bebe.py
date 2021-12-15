from PIL import Image

with Image.open("/Users/jakob/Desktop/baby_filter.png") as im:
  data = im.load()

  out = 0
  wewoo = 1

  for i in range(16, -1, -1):
    for j in range(17):
      print(i,j)
      if data[i, j][0] > 125:
        out += wewoo
      wewoo *= 2
  
  print(out * 17)



