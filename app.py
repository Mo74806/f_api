

from flask import Flask, render_template, request, jsonify, send_file, make_response, send_from_directory


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def mask_image():
    

    


    return "hello"

if __name__ == "__main__":
    app.run(debug=True)

