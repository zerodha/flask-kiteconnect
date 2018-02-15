# Flask-KiteConnect

Flask-KiteConnect is a flask extension to ease up the flask projects using kiteconnect APIs


## Installation

Install the extension with one of the following commands:

```bash
pip install flask-kiteconnect
```

## Usage


```python
from flask import Flask
from flask_kiteconnect import FlaskKiteConnect

app = Flask(__name__)
kiteconnect = FlaskKiteConnect(app)
```

OR the extension way

```python
from flask import Flask
from flask_kiteconnect import FlaskKiteConnect

kiteconnect = FlaskKiteConnect()


# Now initilize it when you create the app
app = Flask(__name__)
kiteconnect.init_app(app)
```
