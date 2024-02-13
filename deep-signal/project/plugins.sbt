resolvers += Resolver.url("sbt-plugins", url("https://repo.scala-sbt.org/scalasbt/sbt-plugin-releases"))(
  Resolver.ivyStylePatterns
)

//addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.14.10")
//addSbtPlugin("net.virtual-void" % "sbt-dependency-graph" % "0.9.2")
//
//addSbtPlugin("org.scoverage" % "sbt-scoverage" % "2.0.8")
//addSbtPlugin("org.scalameta" % "sbt-scalafmt" % "2.4.2")
//addSbtPlugin("ch.epfl.scala" % "sbt-scalafix" % "0.9.27")

addSbtPlugin("org.scoverage" % "sbt-scoverage" % "2.0.9")
addSbtPlugin("org.scoverage" % "sbt-coveralls" % "1.3.11")
addSbtPlugin("org.scalameta" % "sbt-scalafmt" % "2.4.6")
//addSbtPlugin("org.scalastyle" %% "scalastyle-sbt-plugin" % "1.5.0")