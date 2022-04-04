from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello world"

def main():
    app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()