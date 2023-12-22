from flask import Flask
app = Flask('hello-world')
@app.route('/')
def hello():
 return "Hello from the Merge PR deployment this is merged code after review !!!\n"
if __name__ == '__main__':
 app.run(host = '0.0.0.0', port = 8080)
