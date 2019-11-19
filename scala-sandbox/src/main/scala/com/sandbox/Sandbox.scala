package com.sandbox

import scalaz._
import Scalaz._

object Sandbox {
  def main(args: Array[String]): Unit = {
    val f = Kleisli { (x: Int) => (x + 1).some }
    val g = Kleisli { (x: Int) => (x * 100).some }
    println(4.some >>= f >=> g)
    val z = for {
      x <- 1.right
      _ <- "bar".left[String]
    } yield x + 1

    println(z)
  }
}
