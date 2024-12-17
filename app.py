
import os
from model import predict
from flask import (
     Flask, 
     request, 
     render_template)

UPLOAD_FOLDER='./static/image'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_user_files():
    if request.method == 'POST':
        upload_file = request.files['upload_file']
        img_path = os.path.join(UPLOAD_FOLDER,upload_file.filename)
        upload_file.save(img_path)

        jisho, dominant_emotion, emotion_dict, angry, dominant_emotion_per = predict(img_path)

        return render_template('result.html', dominant_emotion=dominant_emotion, emotion_dict=emotion_dict, angry=angry, dominant_emotion_per=dominant_emotion_per, img_path=img_path)


if __name__ == "__main__":
    app.run(debug=True)
        