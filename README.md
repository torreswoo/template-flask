# Template Flask 
template project for Flask Application
[Python Flask](http://flask.pocoo.org/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install project.

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=0
$ python -m flask run
// check "http://0.0.0.0:5000/apidocs/"
```

## init structure
- [Blueprint](http://flask.pocoo.org/docs/1.0/blueprints/#)
- [abseil](https://abseil.io/docs/python/guides/app)
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

## Docker & k8s
- nginx & uWSGI
```bash
# Docker local
$ docker build -t torres-template-flask:0.0.1 . -f Dockerfile
$ docker run -p 80:80 torres-template-flask:0.0.1
$ docker rmi -f torres-template-flask:0.0.1
// check "localhost:80/apidocs"
```
```bash
$ kubectl apply -f k8s/manifest-dev.yml
```

## Swagger
- http://0.0.0.0:5000/apidocs/

## Route

| url |  descrption |  
|---|---|
| GET / | root |
| GET /apidocs | Swagger UI |
| GET /healthz | Health check |
   

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
