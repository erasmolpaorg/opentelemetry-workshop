## Setting up OpenTelemetry with Poetry

Follow these steps to add OpenTelemetry to your Poetry-managed project.

1. Add OpenTelemetry dependencies to your `pyproject.toml` file:

    ```toml
    [tool.poetry.dependencies]
    python = "^3.12"
    flask = "^3.0.3"
    opentelemetry-distro = "*"
    opentelemetry-exporter-otlp = "*"
    ```

2. Install the dependencies using Poetry:

    ```bash
    poetry install
    ```

3. Run the OpenTelemetry bootstrap command:

    ```bash
    poetry run opentelemetry-bootstrap -a install
    ```

4. Run auto instrumentation

    ```bash
    OTEL_SERVICE_NAME=your-service-name \
    OTEL_TRACES_EXPORTER=console,otlp \
    OTEL_METRICS_EXPORTER=console \
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317 \
    poetry run opentelemetry-instrument python app.py
    ```
   