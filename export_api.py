import requests
import time
from datetime import datetime, timedelta

end_date = datetime.utcnow() + timedelta(hours=7)
print(end_date)
PROMETHEUS = "http://localhost:8428/api/v1/query"

query = {
    "query": "sum by (client_ip) (contract_counter[1d])",
    "time": time.mktime(end_date.timetuple())
}
r=requests.get(f"{PROMETHEUS}",params=query)

print(r.json()["data"])
