from flask import Flask, send_from_directory

app = Flask('xss through file download')


# return send_file('xss.pdf'), {'Content-Type': 'text/html; charset=utf-8'}
# sets two content types hence the following approach for sending file.
@app.route('/test1')
def test1():
    # response = send_from_directory(directory='.', filename='xss3')
    # response = send_from_directory(directory='.', filename='xss3.hell')
    # response = send_from_directory(directory='.', filename='xss3.pdf')
    response = send_from_directory(directory='.', filename='xss4')
    return response


# this one patched kid
@app.route('/test2')
def test2():
    response = send_from_directory(directory='.', filename='xss3')
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response


@app.route('/test3')
def test3():
    response = send_from_directory(directory='.', filename='xss3.pdf')
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response


app.run(port=5002)
