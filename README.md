# fastapi-grafana-prometheus-example

Small example of fastapi-grafana-prometheus stack

## Requirements

- Docker
- Docker-compose

## Usage

Clone this repo and run

``` bash
docker-compose up -d
```

Services will be available on following urls:

* Prometheus: http://localhost:9090/
* Grafana: http://localhost:3000/
* FastAPI: http://localhost:8000/  
* FastAPI swagger: http://localhost:8000/docs

**Login and password for Grafana: admin/admin**

On the FastAPI, you can access `/metrics` endpoint to see the data Prometheus is scraping from it.

You can import `test_dashboard.json` to Grafana for some basic graphs. To do it:
1. Open http://localhost:3000/dashboard/import
2. Import `test_dashboard.json`

Or you can create new ones if you want