from flask import Flask
from views import views

app = Flask(__name__) # This initializes the application

app.register_blueprint(views, url_prefix='/views')
# ********************* This is needed for the flask website to run  *********************
if __name__ == '__main__':
    app.run(debug=True)  
      