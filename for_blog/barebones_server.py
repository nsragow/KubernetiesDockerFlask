from flask import Flask

# Create the application object
app = Flask(__name__)


# Associate the return value of the
# landing_page function with the root of the server
@app.route("/")
def landing_page():
    return "Welcome to the landing page"


if __name__ == "__main__": #This avoids running the app on import
    app.run(host="0.0.0.0",port=5000,debug=True)
