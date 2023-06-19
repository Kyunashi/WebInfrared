from flask import Flask, render_template, request
import socket
import lirc

app = Flask(__name__)
client = lirc.Client()
  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        button_num = request.form['buttonId']
        print(f"Button {button_num} pressed!")
        print(client.version())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    

