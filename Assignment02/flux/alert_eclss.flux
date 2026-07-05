import "influxdata/influxdb/monitor"

from(bucket:"lunar-mission")
  |> range(start:-5m)
  |> filter(fn:(r)=>r._measurement=="telemetry-eclss")
  |> filter(fn:(r)=>r._field=="radiation")
  |> monitor.check(
      crit:(r)=>r._value>=5.0,
      warn:(r)=>r._value>=2.1,
      info:(r)=>r._value>=0.3,
      ok:(r)=>r._value<0.3,
      messageFn:(r)=>"Radiation alert: ${r._value}"
  )
