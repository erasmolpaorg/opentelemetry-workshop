
# https://medium.com/insiderengineering/automatic-instrumentation-of-a-python-flask-application-using-opentelemetry-with-jaeger-be50f6530c23
# https://github.com/open-telemetry/opentelemetry-python/blob/stable/docs/examples/auto-instrumentation/server_programmatic.py
from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def main():
    return "Hello, OpenTelemetry!"

if __name__ == "__main__":
    # Set up OpenTelemetry tracing
    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer(__name__)

    # Configure Jaeger exporter
    jaeger_exporter = JaegerExporter(
        agent_host_name='localhost',
        agent_port=6831,
    )

    # Create a BatchSpanProcessor and add the exporter to it
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    # Instrument Flask app with OpenTelemetry
    FlaskInstrumentor().instrument_app(app)

    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)