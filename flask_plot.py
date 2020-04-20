from flask import Flask, send_file, make_response, render_template
from forecast import do_forecast

app = Flask(__name__)

@app.route('/home')
def hello_world():
    return render_template('index.html')

@app.route('/pre', methods = ['GET'])
def sales():
    obj = do_forecast()

    return send_file(obj,
                     attachment_filename = 'plot.png',
                     mimetype = 'image/png')


app.run()