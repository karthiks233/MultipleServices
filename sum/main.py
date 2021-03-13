from flask import Flask, render_template,request


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/sum4',methods=['POST'])
def a():
    n1=request.form['num1']
    n2=request.form['num2']
    x=float(n1)
    y=float(n2)
    r=x*y
    r=str(r)
    return r


@app.route('/')
@app.route('/entry')
def page():
    return render_template('entry.html',title='Are you ready to multiply')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.0', port=8080, debug=True)
