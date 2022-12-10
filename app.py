from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! '
# 范德萨

if __name__ == '__main__':
    app.run()
