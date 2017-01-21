from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'index' + "\n"

@app.route('/oneshot')
def oneshot():
  command = "id"
  encode = ""
  return "oneshot command: " + command + "\n"

@app.route('/rfi')
def rfi():
  url = "http://ninja/export/rfi.py"
  return "rfi: " + url + "\n"

@app.route('/upload/<filename>')
def upload(filename):
  return "upload: " + filename + "\n"

@app.route('/bindshell')
def bindshell():
  return 'bindshell' + "\n"

