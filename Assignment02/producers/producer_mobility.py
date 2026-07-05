import os
import time
import random
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: bytes(v, "utf-8")
)

battery = 100.0
direction = -1

while True:
    # battery cycle
    battery += direction * random.uniform(0.3, 1.2)
    if battery <= 20:
        direction = +1
    elif battery >= 100:
        direction = -1
    battery = round(battery, 2)

    rpm = int(random.uniform(150, 2200))

    if random.random() < 0.10:
        traction = round(random.uniform(0.0, 0.4), 2)
    else:
        traction = round(random.uniform(0.7, 1.0), 2)

    ts = int(time.time() * 1_000_000_000)

    line = (
        f"telemetry-mobility "
        f"battery_voltage={battery},rpm={rpm},traction={traction} {ts}"
    )

    for _ in range(3):
        producer.send("telemetry-mobility", value=line)
        print("MOBILITY ->", line)

    time.sleep(2)

