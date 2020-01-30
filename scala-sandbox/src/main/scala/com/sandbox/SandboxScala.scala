package com.sandbox

import com.twitter.util.Future
import scalaz._
import Scalaz._

object rtf {
  /*
   * Rtf[E, A] is a type alias for ReaderT[Future, E, A].
   *
   * Rtf is a monad transformer that is transforming values through two monads: Reader and Future.
   *
   * Rtf[E, A] lifts a Reader[E, A] into the Future monad, thereby
   * adding environment context reading capability to our Future monad.
   *
   * Essentially `Rtf` wraps an async function of type `E => Future[A]`
   *
   * For more information about the Reader monad, see:
   * <a href="https://docs.google.com/document/d/1MKjE7RMIw0n36cmtnUYkd863vbOnwAEvfKvruUX6Mvc/view#">Dependency Injection and the Reader Monad</a>
   */
  type Rtf[E, A] = ReaderT[Future, E, A]

  object Rtf extends KleisliInstances {
    def apply[E, A](f: E => Future[A]): Rtf[E, A] = Kleisli.kleisli(f)
  }

  implicit object FutureMonad extends Monad[Future] {
    def point[A](a: => A): Future[A] = Future.value(a)

    def bind[A, B](fa: Future[A])(f: A => Future[B]): Future[B] = fa.flatMap(f)
  }

}

object Foo {
  def foo(): String = {
    return ("foo")
  }

  private val baz = "baz"
}

case class Foo() {
  import Foo._

  val bar = Foo.baz

  def baz(): String = {
    return bar
  }

}

object SandboxScala {
  def main(args: Array[String]): Unit = {
    // val a = List(1, 2, 3) <*> List((_: Int) * 0, (_: Int) + 100, (x: Int) => x * x)
    // print(a)
    val f = new Foo()
    println(f.baz())
  }
}
