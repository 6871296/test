import flask
app=flask.app()

t='从未提交'

@app.route('/')
def index():
    return flask.render_template('index.html',t=t)

@app.route('/send')
def send():
    return flask.render_template('send.html')

@app.route('/post_reader')
def postreader():
    t=request.args['text']
    return flask.redirect('/')

app.run()