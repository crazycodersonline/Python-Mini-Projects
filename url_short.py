import pyshorteners

link = "https://www.youtube.com/watch?v=kfk0hZeUgeM&list=PL-sBHWqYN7dV8VvRI3qop_l-GPz94_fWh"

shorturl = pyshorteners.Shortener().tinyurl.short(link)

print(shorturl)