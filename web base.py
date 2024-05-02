from flask import Flask, render_template,send_from_directory
from flask_cors import CORS


app = Flask(__name__,static_folder="static")
CORS(app)
@app.route('/')
def hello_world():
   return render_template(["index.html","example.css"])

# @app.route('/static/css/<path:path>')
# def send_css(path):
#     return send_from_directory('static/css', path)

if __name__ == '__main__':
   app.run(debug=True,port=8000)
