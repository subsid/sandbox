import $ivy.`org.scalaz::scalaz-core:7.2.27`, scalaz._, Scalaz._

println((Option(1) |@| Option(2))(_ + _));
