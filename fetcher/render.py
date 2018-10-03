import flask

def render(data):

    if data['success']:
        rendered = flask.render_template('info.html', 
                title = data['title'], 
                url = data['url'], 
                description = data['description'],
                img = data['image']
                )
    else:
        rendered = flask.render_template('error.html', url = data['url'], msg = data['msg'] )


    return rendered