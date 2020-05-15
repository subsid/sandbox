package com.sandbox

final case class Person(name: String)
final case class Dog(name: String)

// https://www.theguardian.com/info/developer-blog/2016/dec/22/parental-advisory-implicit-content
// Simple typeclass
trait CanChat[A] {
  def chat(a: A): String
}

object ChatOps {
  implicit object ChattyPerson extends CanChat[Person] {
    def chat(person: Person): String = {
      s"Hello, I am a person named ${person.name}"
    }
  }

  implicit object ChattyDog extends CanChat[Dog] {
    def chat(dog: Dog): String = {
      s"Hello, I am a dog named ${dog.name}"
    }
  }

  implicit object String extends CanChat[String] {
    def chat(s: String) = {
      s"chatty $s"
    }
  }

  implicit class ChatUtil[A](a: A) {
    def chat(implicit makesChatty: CanChat[A]): String = {
      makesChatty.chat(a)
    }
  }
}

object ImplicitsSandbox {
  import ChatOps._

  def main(args: Array[String]): Unit = {
    val person = Person("Alex");
    val dog = Dog("Doggy");

    println(person.chat);
    println(dog.chat);
    println("Hello".chat)
  }
}

