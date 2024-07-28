from flask import Flask
from .resources import api 
from .websocket_server import main 

app = Flask(__name__)
api.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

import threading
thread = threading.Thread(target=main)
thread.start()

if __name__ == '__main__':
    app.run(debug=True)

 

#extra code  

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, welcome to packet sniffer!'

# # Add more routes here:
# @app.route('/about')
# def about():
#     return 'This is the about page.'

# @app.route('/users/<username>')
# def greet_user(username):
#     return f'Hello, {username}!'

# if __name__ == '__main__':
#     app.run(debug=True)
