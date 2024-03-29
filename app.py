from flask import Flask, render_template, request
import lirc

app = Flask(__name__)
client = lirc.Client()
  



#def sendIRSignal(button_num):
  #  if button_num == 1:
 #       try:
#            client.send_once("beamer", "KEY_POWER")
#            print("Beamer Power Key")
        

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        button_num = request.form['buttonId']
        print(f"Button {button_num} pressed!")
        print("Lirc Version: " + client.version())
        client.send_once("beamer", "KEY_POWER")
        print("Beamer Power Key Clicked")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    


