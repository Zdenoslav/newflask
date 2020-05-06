from shop import app


if __name__ == '__main__':
    app.jinja_env.cache= {}
    app.run(port=5000,debug=True,threaded=True)
