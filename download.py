from pathlib import Path
import urllib.request

my_file = Path("input.png")
if my_file.exists():
    print("input.png file found")
else:
    print('downloading input.png')
    url = 'https://github.com/initedit-project/trailer.py/raw/master/input.png'  
    urllib.request.urlretrieve(url, 'input.png')  