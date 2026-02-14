from flask import Flask,render_template,request
from yt_download import yt_dld

app = Flask(__name__)
@app.route("/",)
def index_page():
    return render_template('index.html')


@app.route("/download_page",methods = ["POST"])
def download_page():
    # global url
    url = request.form["youtubeUrl"]
    return render_template('download.html',youtube_url = url)

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('youtube_url')
    quality = request.form.get('quality')
    yt = yt_dld(url)
    if quality == '480p':
        yt.video_480p()
    elif quality == '720p':
        yt.video_720p()
    return render_template('success.html',url=url,quality=quality)


if __name__ == '__main__':
    app.run(debug=True)
