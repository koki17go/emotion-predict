from deepface import DeepFace

def predict(input_filename): #predict(input_filename)
  
  objs = DeepFace.analyze(
  img_path = input_filename,   #input_filename,
  actions = ['age', 'gender', 'race', 'emotion'],
  detector_backend = 'mtcnn'  # 他の選択肢: 'dlib', 'retinaface', 'facenet'
  )
  
  jisho = objs[0]
  
  emotion_dict = jisho['emotion']

  angry = emotion_dict['angry']

  dominant_emotion = jisho['dominant_emotion']
  
  dominant_emotion_per = emotion_dict[dominant_emotion]

  return jisho, dominant_emotion, emotion_dict, angry, dominant_emotion_per

#want = predict()

#print(want)

#やること
#辞書になっているものを整理する（感情:%　でリストにする）おそらくvalueがstr型のため、string[]を使うかも
#dominant_emotionの確率を出す

#一回実行してみる