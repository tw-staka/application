from flask import Flask
app = Flask('hello-world-gitops')

@app.route('/')
def hello():
  return "Bonjour tout le monde\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
