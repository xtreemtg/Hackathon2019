from bottle import route, run, template, static_file, request


@route('/', method='GET')
def index():
    return template("index.html")


@route('/static/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='static')


@route('/static/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='static')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)


if __name__ == "__main__":
    main()