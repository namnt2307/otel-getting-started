### python otel-getting-started 

1. Start
```
docker-compose up -d
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
flask run --host 0.0.0.0 --port 8080
```

2. test
* generate sample data
```
curl "http://localhost:8080/getContract?id=hd123431"
curl "http://localhost:8080/getContractUnique?id=hd123431"
```
* goes to localhost:3000, signin with admin/admin
* view report-api dashboard
