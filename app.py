from flask import Flask  

app = Flask(__name__)  

@app.route('/')  
def home():  
    return "Flask berjalan dengan sukses!"  

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)

@app.route("/data")
def data():
    return {"message": "API berjalan dengan sukses!", "status": 200}
