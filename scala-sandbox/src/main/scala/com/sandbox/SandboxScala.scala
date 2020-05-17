package com.sandbox

import cats.effect.IO
import cats.implicits._

object SandboxScala {
  def main(args: Array[String]): Unit = {
    val io1 = IO {
      Thread.sleep(1000)

      42
    }
    println("Foo")

    val io2 = IO {
      Thread.sleep(500)

      21
    }

    val ios = List(io1, io2)

    println(ios.sequence.unsafeRunSync())
  }
}
