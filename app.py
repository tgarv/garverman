from flask import Flask, render_template
import os
import dropbox

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    return 'Coming Soon!'

# @app.route('/gallery')
# def gallery():
#     photos = get_photos()
#     return render_template('gallery.html', photos=photos)

def get_photos():
    photo_urls = [] # TODO add metadata (title and caption) here
    dbx = dropbox.Dropbox('WJAqPX-UcboAAAAAAABBl_HUSU6Tj1iwdWPpdMzZyO0z9768QnxRusoUZm80Kd10')
    for entry in dbx.files_list_folder('').entries:
        link = dbx.sharing_create_shared_link(entry.path_lower)
        url = link.url.replace("dl=0", "dl=1")
        photo_urls.append(url)

    return photo_urls

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)