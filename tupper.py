from PIL import Image

# constants
height = 17
width = 107
startx = 0
starty = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719 # self
starty = 15785084784951999363399610871381700625533184756820024452699685803858851003561871665004527 # baby
flipx = False
flipy = True

def formula(x, y):
    return 0.5 < ((y//17) >> (17*x+(y%17))) % 2


img = Image.new(size=(width, height), mode="RGB")
bitmap = img.load()

for x in range(width):
    for y in range(height):
        y_hat = y if flipy else height-y-1
        x_hat = x if flipx else width-x-1
        bitmap[x_hat, y_hat] = (255, 255, 255) if formula(x + startx, y + starty) else (0, 0, 0)

img.save("bob.png")