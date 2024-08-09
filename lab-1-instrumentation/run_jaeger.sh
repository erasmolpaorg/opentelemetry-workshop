helm repo add jaegertracing https://jaegertracing.github.io/helm-charts
helm repo update
helm install jaeger-tracing jaegertracing/jaeger

kubectl port-forward service/jaeger-tracing-query 16686:16686