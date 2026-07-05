import os
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: bytes(v, "utf-8")
)

cabin_pressure = 101.2

while True:
    external_temp = round(random.uniform(-170, 120), 1)

    p = random.random()
    if p < 0.05:
        radiation = round(random.uniform(5.0, 9.4), 3)
    elif p < 0.20:
        radiation = round(random.uniform(2.1, 2.8), 3)
    else:
        radiation = round(random.uniform(0.06, 0.3), 3)

    cabin_pressure += random.uniform(-0.05, 0.05)
    cabin_pressure = round(cabin_pressure, 2)

    ts = int(time.time() * 1_000_000_000)

    line = (
        f"telemetry-eclss "
        f"external_temp={external_temp},radiation={radiation},cabin_pressure={cabin_pressure} {ts}"
    )

    for _ in range(3):
        producer.send("telemetry-eclss", value=line)
        print("ECLSS ->", line)

    time.sleep(2)