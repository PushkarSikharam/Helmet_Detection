from flask import Flask, render_template,request
import subprocess
app = Flask(__name__)

@app.route('/')
def home4():
    return render_template('home4.html')

@app.route('/about',methods=['GET'])
def about():
   return render_template('about.html')

@app.route('/helmet-tracking', methods=['POST'])
def helmet_tracking():
    if request.method=='POST':
      subprocess.Popen(['python', 'C:\\Users\\Pushkarsikharam\\OneDrive\\Desktop\\III MINI PROJECT\\HELMET_DETECTION-main\\webcam_helmet_detect.py'])
    return "Helmet detection Started...."

@app.route('/number-plate-tracking', methods=['POST'])
def number_plate_tracking():
    if request.method=='POST':
      subprocess.Popen(['python', 'C:\\Users\\Pushkarsikharam\\OneDrive\\Desktop\\III MINI PROJECT\\HELMET_DETECTION-main\\number_plate.py'])
    return "Number plate Recognition Started...."

if __name__ == '__main__':
    app.run(debug=True)
