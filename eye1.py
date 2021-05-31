# from flask import Flask, render_template, Response, request, redirect, url_for
# import tkinter as tk
# import time
# import random
# import speech_recognition as sr
import pyttsx3 as engine
# import threading
# from bs4 import BeautifulSoup 
# import requests 

from flask import Flask, render_template, Response, request, redirect, url_for,flash, session
import tkinter as tk
import time
import random
import speech_recognition as sr
# import pyttsx3
import threading
from werkzeug.utils import secure_filename
import os
from flask_session import Session
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import time
import sys
import requests 
from bs4 import BeautifulSoup 
SESSION_TYPE = 'filesystem'
sess = Session()

global i
global p
app = Flask(__name__,static_url_path='/static')
app.config["TEMPLATES_AUTO_RELOAD"] = True



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/eye/", methods=['POST'])
def index1():
    def fun():
        window = tk.Tk()
        window.configure(background='white')
        window.state("zoomed")
        canvas = tk.Canvas(window, bg="white", width=980, height=580, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas_scroll = tk.Scrollbar(canvas, command=canvas.yview)
        canvas_scroll.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        canvas.configure(yscrollcommand=canvas_scroll.set, scrollregion=())
        i=0
        wrong=0
        engine.speak("Before begning the test kindly keep 6 meter distance from the screen, we will now test the right eye, cover the left eye")
        j=[152,130,108,87,65,43,33,21,15,9]
        for x in j:
            i=i+1
            # speech to text algorithm
            def speech():
                    nonlocal wrong
                    def top():
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            # read the audio data from the default microphone
                            r.adjust_for_ambient_noise(source)
                            print("speak now")       
                            engine.speak("you may speak now")
                            print('hello world')
                            # engine.runAndWait()
                            audio_data = r.record(source, duration=3)
                            print("Recognizing...")
                            try:
                                # convert speech to text
                                text = r.recognize_google(audio_data, language='en-GB')
                                print(type(text))
                                if(((text>='a' and text<= 'z') or (text>='A' and text<='Z')) and (len(text)==1)):
                                    print(len(text))
                                    print(text)
                                    return text 
                                    
                                else:
                                    engine.speak("sorry we could not recognise you said, say it clearly again")
                                    # engine.runAndWait()
                                    return top() 
                                    
                            except:
                                engine.speak("sorry could not recognise ur voice, you will have to say that again")
                                # engine.runAndWait()
                                print("sorry could not recognise ur voice")
                                return top()
                    
                    #Scomparison code
                    for g in op:
                        print(op)
                        d= top()
                        if d.isupper()== False:
                            d= d.upper()
                            print(d)
                        if g != d:
                            wrong = wrong+1
                    

            if wrong !=0:
                print("wrong=", wrong)
                canvas.destroy()
                window.destroy()
                break
            elif i==10 and wrong==0:
                canvas.destroy()
                window.destroy()
                break
                
            #this will call the screen display
            list = ['A','D','F','L','M','N','W','X']
            sampling = random.sample(list, k=5)
            op = sampling
            # here the random letters are generated

            def applytoLabel():
                n = len(op)
                element = ''
                for i in range(n):
                    element = element + op[i] +"   "
                return element
            m=x
            l9 = tk.Label(canvas, text=applytoLabel(),font= ("Optician Sans", m ,'bold'), bg="white").grid(column=1, row=1, sticky='nsew',padx=85, pady=250)
            canvas.create_window(33,33, window=l9, anchor=tk.NW)
            window.after(1,window.update(),speech())
            
        window.mainloop()
        print("number of iterations",i-1) 
        va =[1.00,0.90,0.80,0.70,0.60,0.50,0.40,0.30,0.20,0.10]
        LogMAR = va[i-2] + 0.02 * (wrong)
        print(LogMAR,"LogMAR Units")
        righteye = LogMAR
        wrong =0
        return righteye

    

    def fun1(): 
        window1 = tk.Tk()
        window1.configure(background='white')
        window1.state("zoomed")         
        canvas1 = tk.Canvas(window1, bg="white", width=980, height=580, highlightthickness=0)
        canvas1.pack(fill=tk.BOTH, expand=True)
        canvas1_scroll = tk.Scrollbar(canvas1, command=canvas1.yview)
        canvas1_scroll.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        canvas1.configure(yscrollcommand=canvas1_scroll.set, scrollregion=())
        p=0
        wrong1=0
        engine.speak("Before begning the test kindly keep 6 meter distance from the screen, we will now test your left eye, cover the right eye")
        j=[152,130,108,87,65,43,33,21,15,9]
        for x in j:
            p=p+1
            # speech to text algorithm
            def speech():
                    nonlocal wrong1
                    def top():
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            # read the audio data from the default microphone
                            r.adjust_for_ambient_noise(source)          
                            print("speak now")       
                            engine.speak("you may speak now")
                            # engine.runAndWait()
                            audio_data = r.record(source, duration=3)
                            print("Recognizing...")
                            try:
                                # convert speech to text
                                text = r.recognize_google(audio_data, language='en-GB')
                                print(type(text))
                                if(((text>='a' and text<= 'z') or (text>='A' and text<='Z')) and (len(text)==1)):
                                    print(len(text))
                                    # print(text, "is an Alphabet)
                                    # print(type(text))
                                    print(text)
                                    return text 
                                    
                                else:
                                    engine.speak("sorry we could not recognise you said, say it clearly again")
                                    # engine.runAndWait()
                                    # print(text)
                                    return top() 
                                    
                            except:
                                engine.speak("sorry could not recognise ur voice, you will have to say that again")
                                # engine.runAndWait()
                                print("sorry could not recognise ur voice")
                                return top()

                    #Scomparison code
                    for g in op:
                        print(op)
                        d= top()
                        if d.isupper()== False:
                            d= d.upper()
                            print(d)
                        if g != d:
                            wrong1 = wrong1+1
                    

            if wrong1 !=0:
                print("wrong=", wrong1)
                canvas1.destroy()
                window1.destroy()
                break
            elif p==10 and wrong1==0:
                canvas1.destroy()
                window1.destroy()
                break
                
            #this will call the screen display
            list = ['A','D','F','L','M','N','W','X']
            sampling = random.sample(list, k=5)
            op = sampling
            # here the random letters are generated

            def applytoLabel():
                n = len(op)
                element = ''
                for i in range(n):
                    element = element + op[i] +"   "
                return element
            m=x
            l9 = tk.Label(canvas1, text=applytoLabel(),font= ("Optician Sans", m ,'bold'), bg="white").grid(column=1, row=1, sticky='nsew',padx=85, pady=250)
            canvas1.create_window(33,33, window1=l9, anchor=tk.NW)
            window1.after(1,window1.update(),speech())
            
        window1.mainloop()
        print("number of iterations",p-1) 
        va =[1.00,0.90,0.80,0.70,0.60,0.50,0.40,0.30,0.20,0.10]
        LogMAR1 = va[p-2] + 0.02 * (wrong1)
        print(LogMAR1,"LogMAR Units")
        lefteye= LogMAR1
        wrong1=0
        return lefteye

        
    right=fun()
    
    left=fun1()
    
    
   
    return render_template('index.html',righteye = right, lefteye = left)


@app.route('/webscraping', methods = ['GET', 'POST'])
def webscraping():
    disease_name=''
    if request.method == 'POST':
        diseasename = request.form["browser"]
        print(diseasename)
        print("hi")
    print(diseasename) 
    disease = diseasename   
    URL = "https://www.nhs.uk/conditions/"
    r = requests.get(URL) 
    i=0   
    soup = BeautifulSoup(r.content, 'html5lib')  

    names = []
    link = []

    for item in soup.findAll('a', {'class': 'nhsuk-list-panel__link'}):
        names.append(item.get_text(strip=True))

    for item in soup.findAll('li', attrs = {'class':'nhsuk-list-panel__item'}):
        link.append(item.a['href'] )

    for j in names:
        if j == disease :
            print(j)
            break
        else:
            i= i+1

    pandu ='https://www.nhs.uk/'+link[i]

    print(pandu)
    URL1 = pandu
    r1 = requests.get(URL1) 
    soup = BeautifulSoup(r1.content, 'html5lib')  
    table = soup.findAll('section')  

    quotes = []  
    for row in table:  
        na = row.get_text()   
        quotes.append(na) 

    pop= ''
    for fo in quotes:
        pop= pop + fo

    print(pop)
    return render_template('index.html', pop= pop)


app.config['UPLOAD_FOLDER'] = 'C://Users//Mahesh//Desktop//new env//env//data//pogo'
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      flash('file uploaded successfully')
      status = 'file uploaded successfully'
      return render_template('index.html', status= status)


@app.route('/finder', methods = ['GET', 'POST'])
def finderpic(): 
    start = time.time()
    #Define Path
    model_path = './models/model.h5'
    model_weights_path = './models/weights.h5'
    test_path = 'data/pogo'

    #Load the pre-trained models
    model = load_model(model_path)
    model.load_weights(model_weights_path)

    #Define image parameters
    img_width, img_height = 150, 150

    #Prediction Function
    def predict(file):
        x = load_img(file, target_size=(img_width,img_height))
        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        array = model.predict(x)
        result = array[0]
        #print(result)
        answer = np.argmax(result)
        if answer == 0:
            print("Predicted: cataract")
        elif answer == 1:
            print("Predicted:conjunctivities ")
        elif answer == 2:
            print("Predicted: eyelid cyst")
        elif answer == 3:
            print("Predicted: jaundise")

        return answer

    #Walk the directory for every image
    for i, ret in enumerate(os.walk(test_path)):
        for i, filename in enumerate(ret[2]):
            if filename.startswith("."):
                continue
        
            print(ret[0] + '/' + filename)
            result = predict(ret[0] + '/' + filename)
            print(result)
    if result == 0:
        predict=' cataract'
    elif result == 1:
        predict= 'conjunctivities' 
    elif result == 2:
        predict= 'eyelid cyst'
    elif result == 3:
        predict= 'jaundise'

    print(predict)
    #Calculate execution time
    end = time.time()
    dur = end-start

    if dur<60:
        print("Execution Time:",dur,"seconds")
    elif dur>60 and dur<3600:
        dur=dur/60
        print("Execution Time:",dur,"minutes")
    else:
        dur=dur/(60*60)
        print("Execution Time:",dur,"hours")

    folder_path = (r'C://Users//Mahesh//Desktop//new env//env//data//pogo')
    test = os.listdir(folder_path)
    for images in test:
        if images.endswith(('jpg','jpeg','png')):
            os.remove(os.path.join(folder_path, images))

    print(' images deleted')
    return render_template('index.html',predict = predict)
      



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)
    app.run(debug=True)