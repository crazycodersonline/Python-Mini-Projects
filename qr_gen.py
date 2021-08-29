

import qrcode

data = "https://www.youtube.com/channel/UCWBJJ2rkQ3UF9eAHENnj2Rg"

img = qrcode.make(data)
img.save("CrazyCodersyt.png")

