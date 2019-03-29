from flask import Flask
app = Flask('hello-world-gitops')

@app.route('/')
def hello():
  return "Hello tout le monde, Version: 2\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
