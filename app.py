from flask import Flask, render_template
import os
import dropbox

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/v2')
def index2():
    return render_template('index2.html')

@app.route('/rsvp')
def rsvp():
    return render_template('rsvp.html')

@app.route('/request_electronic_invitation')
def request_electronic_invitation():
    return render_template('request_electronic_invitation.html')

@app.route('/our_story')
def our_story():
    return render_template('our_story.html')

@app.route('/regrets')
def regrets():
    return render_template('regrets.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/wedding_info')
def wedding_info():
    return render_template('base.html')

@app.route('/lodging_info')
def lodging_info():
    return render_template('base.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)