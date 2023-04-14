from flask import Flask, request
from static import CmdUtil, InfoGetter

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    return 'hello'


@app.route('/connect', methods=['GET'])
def connect_and_work():
    src = request.args.get('src')
    dst = request.args.get('dst')
    num = request.args.get('num')
    info_str = CmdUtil.connect_and_work(src, dst, num)

    return InfoGetter.getinfo(info_str)


if __name__ == '__main__':
    app.run()