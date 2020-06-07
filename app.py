
from PIL import Image
import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify, send_file, make_response, send_from_directory
from torchvision.utils import save_image

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def mask_image():
    

    


    return send_file("hello", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

