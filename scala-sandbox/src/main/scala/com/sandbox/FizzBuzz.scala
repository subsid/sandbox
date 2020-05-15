package com.sandbox

trait Monoid[A] {
  val empty: A
  def combine(x: A, y: A): A
}


object MonoidOps {
  implicit val stringMonoid = new Monoid[String] {
    val empty: String = ""
    def combine(x: String, y: String) = x + y;
  }

  implicit val intMonoid = new Monoid[Int] {
    val empty = 0
    def combine(x: Int, y: Int) = x + y;
  }

  implicit def listMonoid[A] = new Monoid[List[A]] {
    val empty = List()
    def combine (x: List[A], y: List[A]) = x ++ y
  }

  implicit def optionMonoid[A](implicit am: Monoid[A]): Monoid[Option[A]] = new Monoid[Option[A]] {
    val empty = None
    def combine(x: Option[A], y: Option[A]) = {
      (x, y) match {
        case (Some(x), Some(y)) => Some(am.combine(x, y))
        case (Some(_), None) => x
        case (None, Some(_)) => y
        case (None, None) => None
      }
    }
  }

  implicit def functionMonoid[A, B](implicit bm: Monoid[B]) = new Monoid[A => B] {
    val empty = _ => bm.empty
    def combine(f: A => B, g: A => B): A => B = {
      i => bm.combine(f(i), g(i))
    }
  }

  implicit def foldRight[A](la: List[A])(implicit am: Monoid[A]): A = {
    la.foldRight(am.empty)(am.combine)
  }
}

object FizzBuzz {
  import MonoidOps._

  def fizz: Int => Option[String] = x => if (x % 3 == 0) Some("fizz") else None
  def buzz: Int => Option[String] = x => if (x % 5 == 0) Some("buzz") else None

  def fizzbuzz = foldRight(List(fizz, buzz))

  def fbOrInt(i: Int): String = {
    fizzbuzz(i).getOrElse(s"${i}")
  }

  def main(args: Array[String]): Unit = {
    val results: List[String] = (1 until 100).toList map fbOrInt
    print(results)
  }

}

