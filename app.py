from flask import Flask, render_template
import os
import dropbox

app = Flask(__name__)
local_files = False


@app.route('/')
def index():
    return render_template('index.html', local_files=local_files)


@app.route('/rsvp')
def rsvp():
    return render_template('rsvp.html', local_files=local_files)


@app.route('/request_electronic_invitation')
def request_electronic_invitation():
    return render_template('request_electronic_invitation.html', local_files=local_files)


@app.route('/our_story')
def our_story():
    return render_template('our_story.html', local_files=local_files)


@app.route('/regrets')
def regrets():
    return render_template('regrets.html', local_files=local_files)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html', local_files=local_files)


@app.route('/wedding_info')
def wedding_info():
    return render_template('base.html', local_files=local_files)


@app.route('/lodging_info')
def lodging_info():
    return render_template('base.html', local_files=local_files)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # app.run()
    app.run(host='0.0.0.0', port=port)