package com.sandbox

import com.typesafe.config._

object HoconTest {

  def main(args: Array[String]) = {
    val conf = ConfigFactory.load()
    println(conf.getInt("foo"))
//    println("The answer is: " + conf.getString("simple-app.answer"))
  }
}
