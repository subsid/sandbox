import $ivy.`com.lihaoyi::requests:0.6.5`

def retry[T](max: Int = 50, delay: Int = 100)(f: => T): T = {
  var tries: Int  = 0
  var result: Option[T] = None
  var backoffTime = delay;
  while (result.isEmpty) {
    try {
      result = Some(f)
    } catch {
      case e: Throwable =>
        tries += 1
        if (tries > max) throw e
        else {
          println(s"failed, retry #$tries")
          println(s"backoff, #$backoffTime")
          Thread.sleep(backoffTime)
          backoffTime *= 2
        }
    }
  }
  result.get
}

val httpbin = "https://httpbin.org"
var tries = 0

retry(max = 5) {
  requests.get(
      s"$httpbin/status/200,400,500"
    )
}

