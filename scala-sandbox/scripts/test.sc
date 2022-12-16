// Implicits
class Foo(val value: Int)

def bar(implicit foo: Foo) = foo.value + 10

// implicit val fooey = new Foo(1);
// bar # This works

trait StrParser[T] {
  def parser(s: String): T
}

object StrParser {
  implicit object ParseInt extends StrParser[Int] { def parser(s: String): Int = s.toInt }
  implicit object ParseBoolen extends StrParser[Boolean] { def parser(s: String): Boolean = s.toBoolean }
  implicit object ParseDouble extends StrParser[Double] { def parser(s: String): Double = s.toDouble }
  implicit def ParseSeq[T](implicit p: StrParser[T]) = new StrParser[Seq[T]] {
    def parser(s: String) = s.split(",").toSeq.map(p.parser)
  }
}

def parse[T](s: String)(implicit parser: StrParser[T]) = {
  parser.parser(s)
}

val args = Seq("123", "5.7", "true", "10,20,30")

println(parse[Int](args(0)))
println(parse[Boolean](args(2)))
println(parse[Seq[Int]](args(3)))
