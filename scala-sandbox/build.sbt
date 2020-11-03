lazy val hello = (project in file("."))
  .settings(
    name := "Hello",
    libraryDependencies += "com.lihaoyi" %% "requests" % "0.6.5",
    libraryDependencies +=  "org.scalatest" %% "scalatest" % "3.2.0" % "test"
  )

