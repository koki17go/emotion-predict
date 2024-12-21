from deepface import DeepFace

def predict(input_filename): #predict(input_filename)
  
  objs = DeepFace.analyze(
  img_path = input_filename,   #input_filename,
  actions = ['age', 'gender', 'race', 'emotion'],
  detector_backend = 'mtcnn'  # 他の選択肢: 'dlib', 'retinaface', 'facenet'
  )
  
  jisho = objs[0]
  
  emotion_dict = jisho['emotion']

  angry_f = emotion_dict['angry']
  angry = int(angry_f)

  disgust_f = emotion_dict['disgust']
  disgust = int(disgust_f)

  fear_f = emotion_dict['fear']
  fear = int(fear_f)

  happy_f = emotion_dict['happy']
  happy = int(happy_f)

  sad_f = emotion_dict['sad']
  sad = int(sad_f)

  surprise_f = emotion_dict['surprise']
  surprise = int(surprise_f)

  neutral_f = emotion_dict['neutral']
  neutral = int(neutral_f)

  dominant_emotion = jisho['dominant_emotion']
  
  dominant_emotion_per = emotion_dict[dominant_emotion]

  return jisho, dominant_emotion, angry, disgust, fear, happy, sad, surprise, neutral, dominant_emotion_per

#want = predict()

#print(want)

#やること
#辞書になっているものを整理する（感情:%　でリストにする）おそらくvalueがstr型のため、string[]を使うかも
#dominant_emotionの確率を出す

#一回実行してみる
#