import "influxdata/influxdb/monitor"

from(bucket:"lunar-mission")
  |> range(start:-5m)
  |> filter(fn:(r)=>r._measurement=="telemetry-comms")
  |> filter(fn:(r)=>r._field=="snr")
  |> monitor.check(
      crit:(r)=>r._value<8,
      warn:(r)=>r._value<12,
      info:(r)=>r._value<18,
      ok:(r)=>r._value>=18,
      messageFn:(r)=>"SNR degraded: ${r._value}"
  )
