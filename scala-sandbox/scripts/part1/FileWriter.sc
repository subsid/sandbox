import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.FileWriter
import java.io.FileReader

def withFileWriter[T](fileName: String, writerCb: BufferedWriter => T) = {
  val writer = new BufferedWriter(new FileWriter(fileName))
  try writerCb(writer)
  finally writer.close()
}

def withFileReader[T](fileName: String, readerCb: BufferedReader => T) = {
  val reader = new BufferedReader(new FileReader(fileName))
  try readerCb(reader)
  finally reader.close()
}

val fileName = "hello.txt"

withFileWriter(fileName, writer => {
    writer.write("Hello\n"); writer.write("World!")
})

val result = withFileReader(fileName, reader => reader.readLine() + "\n" + reader.readLine())

assert(result == "Hello\nWorld!")

