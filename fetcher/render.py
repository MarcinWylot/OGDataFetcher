import flask

def render(data):
    """Renders a template from the template folder with the data fetched from the website.

    Parameters
    ----------
    data : dictionary
        data fetched from the website
        
    Returns
    -------
    flask.render_template
        Rendered template 
    """

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