from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # This is the line we will modify later
    print("User authentication module placeholder")

    return 'Hello, World from main!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)