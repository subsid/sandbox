package com.sandbox

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
    val f = new Foo()
    println(f.baz())
  }
}
