from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        button_num = request.form['buttonId']
        print(f"Button {button_num} pressed!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
