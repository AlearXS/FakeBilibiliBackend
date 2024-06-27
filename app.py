from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/video/av<int:id>')
def video(id):
    video_filename = f'av{id}.mp4'  # 假设视频文件命名为 av{id}.mp4
    return send_from_directory('static/videos', video_filename)

@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
