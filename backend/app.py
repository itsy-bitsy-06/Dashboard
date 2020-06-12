import os
from flask import Flask, send_file
from flask_cors import CORS
from flask_gzip import Gzip
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from Config import DevelopmentConfig
import Models
import Controllers

app = Flask(__name__, static_url_path='', static_folder='./Ui')
app.config.from_object(DevelopmentConfig)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
Gzip(app)

# Initialize database and Apis
Controllers.initialize(app)
Models.initialize(app)
print(app.url_map)

# When routes dont match to anything, send index.html
@app.errorhandler(404)
def not_found_error(error):
    return send_file('./Ui/index.html')

if __name__=='__main__':
    print(f'Listening on all interfaces on port 8888')
    app.run(host='0.0.0.0', port=8888, use_reloader=False)
