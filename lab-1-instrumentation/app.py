from flask import Flask
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.exporter.prometheus import PrometheusMetricsExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.instrumentation.flask import BaseInstrumentor
from prometheus_client import start_http_server
import time

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def main():
    return "Hello, OpenTelemetry with Prometheus!"

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

    # Instrument Flask app with OpenTelemetry for tracing
    FlaskInstrumentor().instrument_app(app)

    # Set up OpenTelemetry metrics
    metrics.set_meter_provider(MeterProvider())

    # Configure Prometheus exporter
    prometheus_exporter = PrometheusMetricsExporter()
    metric_reader = PeriodicExportingMetricReader(prometheus_exporter)
    metrics.get_meter_provider().add_metric_reader(metric_reader)

    # Start Prometheus HTTP server
    start_http_server(8000)

    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)