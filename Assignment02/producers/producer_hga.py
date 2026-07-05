import os
import time
import random
import math
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: bytes(v, "utf-8")
)

while True:
    snr = round(random.uniform(5, 30), 2)

    ber = round(max(0.000001, (1 / (snr + 0.1)) * random.uniform(0.6, 3.0)), 6)

    latency = round(random.uniform(150, 900), 1)

    ts = int(time.time() * 1_000_000_000)

    line = (
        f"telemetry-comms "
        f"snr={snr},ber={ber},latency={latency} {ts}"
    )

    for _ in range(3):
        producer.send("telemetry-comms", value=line)
        print("HGA ->", line)

    time.sleep(2)

