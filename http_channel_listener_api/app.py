from flask import Flask
import yaml
import urllib.request

# set up the flask module
app = Flask(__name__)

# import settings
with open(r'.cfg.yml') as file:
    cfg = yaml.safe_load(file)

url = cfg['url']

# replace this with the trigger of your choice
trigger_string = 'Uit eigen voorraad leverbaar. Levertijd: 1 dag'
tsb = trigger_string.encode()

# when visit localhost:5000 what do you want it to return?
@app.route('/')
def hello():
    page = urllib.request.urlopen(url)
    load_page = page.read()
    if tsb in load_page:
        return "True"
    return "False"

# main function do python app.py to run it
if __name__ == '__main__':
    app.run()