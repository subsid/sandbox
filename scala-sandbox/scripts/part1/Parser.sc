def parseFromString[T: StrParser](s: String): T =
  StrParser[T].parse(s)

def parseFromConsole[T: StrParser]: T =
  StrParser[T].parse(scala.Console.in.readLine())

trait StrParser[T] {
  def parse(s: String): T
}

object StrParser {
  @inline def apply[T: StrParser]: StrParser[T] = implicitly[StrParser[T]]

  implicit val intParser = new StrParser[Int] {
    def parse(s: String) = s.toInt
  }

  implicit val boolParser = new StrParser[Boolean] {
    def parse(s: String)  = s.toBoolean
  }

  implicit val doubleParser = new StrParser[Double] {
    def parse(s: String) = s.toDouble
  }

  implicit def seqParser[T: StrParser] = new StrParser[Seq[T]] {
    def parse(s: String) = s.split(",").toSeq.map(StrParser[T].parse)
  }

  implicit def tupleParser[T: StrParser, V: StrParser] = new StrParser[(T, V)] {
    def parse(s: String) = {
      val Array(left, right) = s.split("=")
      (StrParser[T].parse(left), StrParser[V].parse(right))
    }
  }
}

// val args = Seq("123", "true", "7.5")
// val myInt = parseFromString[Int](args(0))
// val myBoolean = parseFromString[Boolean](args(1))
// val myDouble = parseFromString[Double](args(2))
// val mySeqDouble = parseFromString[Seq[Double]]("1,2.2,3,4")
// val myTupleDouble = parseFromString[(Double, Double)]("1=2")
// val myDoubleConsole = parseFromConsole[Double]


val mySeqTuplDouble = parseFromString[Seq[Boolean]]("[true,false,true]")

