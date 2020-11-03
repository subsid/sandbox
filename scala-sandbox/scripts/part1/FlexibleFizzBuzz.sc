def flexibleFizzBuzz(cb: String => Unit) = {
  for (i <- Range(1, 100)) {
    if ((i % 3) == 0 && (i % 5) == 0) cb("FizzBuzz")
    else if ((i % 3) == 0) cb("Fizz")
    else if ((i % 5) == 0) cb("Buzz")
    else cb(s"$i")
  }
}

var i = 0
val output = new Array[String](100)

flexibleFizzBuzz{s =>
  output(i) = s
  i += 1
}

assert(
  output.take(15).sameElements(
    Array(
      "1",
      "2",
      "Fizz",
      "4",
      "Buzz",
      "Fizz",
      "7",
      "8",
      "Fizz",
      "Buzz",
      "11",
      "Fizz",
      "13",
      "14",
      "FizzBuzz"
    )
  )
)
