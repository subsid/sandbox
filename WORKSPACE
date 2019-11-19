rules_scala_version="26cf9b74fc46f1e9a970c97837447549ed7257b6" # update this as needed

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "io_bazel_rules_scala",
    strip_prefix = "rules_scala-%s" % rules_scala_version,
    type = "zip",
    url = "https://github.com/bazelbuild/rules_scala/archive/%s.zip" % rules_scala_version,
)

load("@io_bazel_rules_scala//scala:toolchains.bzl", "scala_register_toolchains")
scala_register_toolchains()

load("@io_bazel_rules_scala//scala:scala.bzl", "scala_repositories")
scala_repositories((
    "2.12.10",
    {
        "scala_compiler": "cedc3b9c39d215a9a3ffc0cc75a1d784b51e9edc7f13051a1b4ad5ae22cfbc0c",  # scala-compiler-2.12.10.jar
        "scala_library": "0a57044d10895f8d3dd66ad4286891f607169d948845ac51e17b4c1cf0ab569d",  # scala-library-2.12.10.jar
        "scala_reflect": "56b609e1bab9144fb51525bfa01ccd72028154fc40a58685a1e9adcbe7835730",  # scala-reflect-2.12.10.jar
        "scrooge_core": "3c9021636ba28198bf05e9d035c12a0c349b905c55c3043f8437a2c315c9b448",  # scrooge-core_2.12-19.10.0.jar
        "scrooge_generator": "45f60c4bf2d58baac24d67ed8d5ae4c4d5837129ec15377d5002e1e6d7440ff2",  # scrooge-generator_2.12-19.10.0.jar
    },
))


protobuf_version="09745575a923640154bcf307fba8aedff47f240a"
protobuf_version_sha256="416212e14481cff8fd4849b1c1c1200a7f34808a54377e22d7447efdf54ad758"

http_archive(
    name = "com_google_protobuf",
    url = "https://github.com/protocolbuffers/protobuf/archive/%s.tar.gz" % protobuf_version,
    strip_prefix = "protobuf-%s" % protobuf_version,
    sha256 = protobuf_version_sha256,
)

# bazel-skylib 0.8.0 released 2019.03.20 (https://github.com/bazelbuild/bazel-skylib/releases/tag/0.8.0)
skylib_version = "0.8.0"
http_archive(
    name = "bazel_skylib",
    type = "tar.gz",
    url = "https://github.com/bazelbuild/bazel-skylib/releases/download/{}/bazel-skylib.{}.tar.gz".format (skylib_version, skylib_version),
    sha256 = "2ef429f5d7ce7111263289644d233707dba35e39696377ebab8b0bc701f7818e",
)

# Bazel-deps for java and scala deps
load("//third_party:workspace.bzl", "maven_dependencies")

maven_dependencies()
