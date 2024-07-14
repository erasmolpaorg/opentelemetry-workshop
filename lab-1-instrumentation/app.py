from flask import Flask
app = Flask(__name__)

# https://medium.com/insiderengineering/automatic-instrumentation-of-a-python-flask-application-using-opentelemetry-with-jaeger-be50f6530c23
# https://github.com/open-telemetry/opentelemetry-python/blob/stable/docs/examples/auto-instrumentation/server_programmatic.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello, OpenTelemetry!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)