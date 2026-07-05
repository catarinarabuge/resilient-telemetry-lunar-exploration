import "influxdata/influxdb/monitor"

from(bucket: "lunar-mission")
  |> range(start: -5m)
  |> filter(fn: (r) => r._measurement == "telemetry-mobility")
  |> filter(fn: (r) => r._field == "battery_voltage")
  |> monitor.check(
      crit: (r) => r._value < 20,
      warn: (r) => r._value < 40,
      info: (r) => r._value < 60,
      ok:   (r) => r._value >= 60,
      messageFn: (r) => "Battery voltage alert: ${r._value}"
  )

