rules_scala_version = "26cf9b74fc46f1e9a970c97837447549ed7257b6"  # update this as needed

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

protobuf_version = "09745575a923640154bcf307fba8aedff47f240a"

protobuf_version_sha256 = "416212e14481cff8fd4849b1c1c1200a7f34808a54377e22d7447efdf54ad758"

http_archive(
    name = "com_google_protobuf",
    sha256 = protobuf_version_sha256,
    strip_prefix = "protobuf-%s" % protobuf_version,
    url = "https://github.com/protocolbuffers/protobuf/archive/%s.tar.gz" % protobuf_version,
)

# bazel-skylib 0.8.0 released 2019.03.20 (https://github.com/bazelbuild/bazel-skylib/releases/tag/0.8.0)
skylib_version = "0.8.0"

http_archive(
    name = "bazel_skylib",
    sha256 = "2ef429f5d7ce7111263289644d233707dba35e39696377ebab8b0bc701f7818e",
    type = "tar.gz",
    url = "https://github.com/bazelbuild/bazel-skylib/releases/download/{}/bazel-skylib.{}.tar.gz".format(skylib_version, skylib_version),
)

# Bazel-deps for java and scala deps
# load("//third_party:workspace.bzl", "maven_dependencies")

# maven_dependencies()
# load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

RULES_JVM_EXTERNAL_TAG = "3.0"

RULES_JVM_EXTERNAL_SHA = "62133c125bf4109dfd9d2af64830208356ce4ef8b165a6ef15bbff7460b35c3a"

http_archive(
    name = "rules_jvm_external",
    sha256 = RULES_JVM_EXTERNAL_SHA,
    strip_prefix = "rules_jvm_external-%s" % RULES_JVM_EXTERNAL_TAG,
    url = "https://github.com/bazelbuild/rules_jvm_external/archive/%s.zip" % RULES_JVM_EXTERNAL_TAG,
)

load("@rules_jvm_external//:defs.bzl", "maven_install")
load("@rules_jvm_external//:specs.bzl", "maven")

maven_install(
    artifacts = [
        "junit:junit:4.12",
        "org.hamcrest:hamcrest-library:1.3",
        "com.twitter:finatra-http_2.12:jar:20.4.1",
        maven.artifact(
            group = "com.twitter",
            artifact = "finatra-http_2.12",
            version = "20.4.1",
        ),
    ],
    repositories = [
        # Private repositories are supported through HTTP Basic auth
        "http://username:password@localhost:8081/artifactory/my-repository",
        "https://jcenter.bintray.com/",
        "https://maven.google.com",
        "https://repo1.maven.org/maven2",
    ],
)
