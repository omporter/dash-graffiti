from flask import Flask
from lib.graffiti import generate_graffiti_address

app = Flask(__name__)

@app.route('/')
def index():
	return generate_graffiti_address("Heroku Test")

if __name__ == "__main__":
	app.run()