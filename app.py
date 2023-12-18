import os
from flask import Flask, render_template

app = Flask('hello-world')

@app.route('/')
def hello():
    current_directory = os.getcwd()
    template_path = os.path.join(current_directory, 'index.html')
    return render_template(template_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
