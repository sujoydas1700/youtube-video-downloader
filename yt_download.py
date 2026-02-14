import yt_dlp

def download(url,ydl_opts):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        print('done')
    except Exception as e:
        print(e)

class yt_dld:
    def __init__(self,url):
        self.url = url

    def video_480p(self):
        ydl_opts = {
            'format': 'best[ext=mp4][height<=480]',
            'outtmpl': '%(title)s_480p.%(ext)s',
        }
        download(self.url,ydl_opts)
    
    def video_720p(self):
        ydl_opts = {
            'format': 'best[ext=mp4][height<=720]',
            'outtmpl': '%(title)s_720p.%(ext)s',
        }
        download(self.url,ydl_opts)
