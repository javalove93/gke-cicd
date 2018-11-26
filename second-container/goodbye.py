from flask import Flask
app = Flask(__name__)

@app.route("/")
def goodbye():
    return "Goodbye /\n"

@app.route("/goodbye")
def goodbye2():
    return "Goodbye /goodbye\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6666)

