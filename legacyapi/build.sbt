name := """legacy_api"""

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayJava)

scalaVersion := "2.11.1"

libraryDependencies ++= Seq(
  javaJdbc,
  javaEbean,
  cache,
  javaWs,
  "com.jayway.restassured" % "rest-assured" % "2.3.1",
  "com.google.code.gson" % "gson" % "2.3"
//  "com.wordnik" %% "swagger-play2" % "1.3.7" exclude("org.reflections", "reflections")
)
