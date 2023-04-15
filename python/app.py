from random import randint, choice
from flask import Flask, request
from otel_config import meter
from enum import Enum


ct_facts = ["true", "false"]
ct_unique_facts = ["true", "false"]
client_ip = [
    "127.0.0.1",
    "172.24.178.200",
    "172.27.11.165",
    "192.168.1.32",
    "172.27.11.98",
    "172.24.187.43",
    "172.24.187.41",
    "172.24.186.41",
    "172.24.189.41",
]

app = Flask(__name__)

contract_counter = meter.create_counter(
    "contract_counter",
    description="The number of rolls by roll value",
)

unique_contract_counter = meter.create_counter(
    "unique_contract_counter",
    description="The number of rolls by roll value",
)


@app.route("/getContract", methods=["GET"])
def get_contract():
    args = request.args
    contract_id = args.get("id")
    l_ct_status = choice(ct_facts)
    l_ct_unique = choice(ct_unique_facts)
    l_client_ip = choice(client_ip)
    contract_counter.add(
        1,
        {
            "ct_status": l_ct_status,
            "client_ip": l_client_ip,
        },
    )
    res = f"id: {contract_id} ct: {l_ct_status}  ip {l_client_ip}"
    return str(res)


@app.route("/getContractUnique", methods=["GET"])
def get_unique_contract():
    args = request.args
    contract_id = args.get("id")
    l_ct_unique = choice(ct_unique_facts)
    l_client_ip = choice(client_ip)
    unique_contract_counter.add(
        1,
        {
            "ct_unique": l_ct_unique,
            "client_ip": l_client_ip,
        },
    )
    res = f"id: {contract_id} ct_unique: {l_ct_unique}, ip {l_client_ip}"
    return str(res)
