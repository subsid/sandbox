import java.util.concurrent.Executors

import scala.concurrent.{ExecutionContext, Future, Await, TimeoutException}
import scala.concurrent.duration._
import scala.language.postfixOps
import scala.util.Try
import scala.util.{Success, Failure}


/**
 * HTTP library
 *
 * getBatch(requests: BatchRequest, batchSize: Int): Future[BatchReponse]
 *
 * Data case classes
 * BatchRequest(requests: List[Request])
 * BatchResponse(responses: List[RawResponse])
 * RawResponse(value: String)

 * Part 2
 * ParsedResponse(value: Int)
 * ParsedResponse.parser: RawResponse => Try[ParsedResponse]
 */


class RequestBatcher(implicit ec: ExecutionContext) {

  /**
   * Should fail if any call to Http.getBatch fails
   *
   *
   * Helpful docs
   * https://www.scala-lang.org/api/2.12.2/scala/concurrent/Future.html
   * https://www.scala-lang.org/api/2.12.3/scala/collection/immutable/List.html
   */
  def requestBatch(requests: List[Request],
                   batchSize: Int): Future[List[RawResponse]] = {

     val batchRequests: List[BatchRequest] = requests
                                              .grouped(batchSize)
                                              .toList
                                              .map(BatchRequest.apply)


     val responseBatches: List[Future[List[RawResponse]]] = batchRequests.map(getResponse)
     val responses: Future[List[List[RawResponse]]] = Future.traverse(responseBatches)(transformFuture(_))

     ???
  }

  def getResponse(batchRequest: BatchRequest): Future[List[RawResponse]] =
    Http.getBatch(batchRequest)
      .map(_.responses)

  def transformFuture(fr: Future[List[RawResponse]]): Future[List[RawResponse]] = fr

  def parseResponse(rawResponse: RawResponse): Try[ParsedResponse] = ???
}


object Solution extends App {
  implicit val ec: scala.concurrent.ExecutionContext = scala.concurrent.ExecutionContext.global
  val batcher = new SampleRequestBatcher()

  val response = batcher.requestBatch(List(ValidRequest("1"), ValidRequest("2"), ValidRequest("3")), 2)
  println(Await.result(response, 2 seconds))
}


//=============================IGNORE=======================================================================================================================


/*
 * HTTP service that supports batch requests.
 */
object Http {
  def getBatch(batch: BatchRequest)(implicit ec: ExecutionContext): Future[BatchResponse] =
    Future(BatchResponse(batch.requests.map(handleRequest)))

  private def handleRequest(request: Request): RawResponse =
    request match {
      case v: ValidRequest => RawResponse(v.value)
      case BatchFail       => throw new TimeoutException("Http request timeout")
    }
}

/*
 * Model
 */
sealed trait Request
case class ValidRequest(value: String) extends Request
case object BatchFail extends Request

/* Raw, unparsed response from the client */
final case class RawResponse(value: String)
/* Successful parsed case */
final case class ParsedResponse(value: Int)
case object ParsedResponse {
  val parser: String => Try[ParsedResponse] = s =>
  Try(ParsedResponse(s.toInt))
}
final case class BatchRequest(requests: List[Request])
final case class BatchResponse(responses: List[RawResponse])







import java.util.concurrent.Executors

import scala.concurrent.{ExecutionContext, Future, Await, TimeoutException}
import scala.concurrent.duration._
import scala.language.postfixOps
import scala.util.Try
import scala.util.{Success, Failure}


// ==================================================================
// =================== Sample Implementation ========================

class SampleRequestBatcher(implicit ec: ExecutionContext) {
 /**
   * 1) Should fail if any call to Http.getBatch fails
   * 2) Should ignore Http.getBatch TimeoutException failures
   * 3) Should ignore parsing failures and return successful ParsedResponses
   *
   * Helpful docs
   * https://www.scala-lang.org/api/2.12.2/scala/concurrent/Future.html
   * https://www.scala-lang.org/api/2.12.3/scala/collection/immutable/List.html
   * https://www.scala-lang.org/api/2.9.3/scala/util/Try.html
   */
  def requestBatch(requests: List[Request],
                   batchSize: Int): Future[List[ParsedResponse]] = {

     val batchRequests: List[BatchRequest] = requests
                                              .grouped(batchSize)
                                              .toList
                                              .map(BatchRequest.apply)


     val responseBatches: List[Future[List[RawResponse]]] = batchRequests.map(getResponse)
     val responses: Future[List[List[ParsedResponse]]] = Future.traverse(responseBatches)(transformFuture(_))

     responses.map(_.flatten)
  }

  def getResponse(batchRequest: BatchRequest): Future[List[RawResponse]] =
    Http.getBatch(batchRequest)
      .map(_.responses)

  def transformFuture(fr: Future[List[RawResponse]]): Future[List[ParsedResponse]] = {
    fr.map(parseResponses(_))
    .recover {
      case e: TimeoutException => Nil
    }
  }

  def parseResponses(rawResponses: List[RawResponse]): List[ParsedResponse] = {
    rawResponses
      .map((rr) => ParsedResponse.parser(rr.value))
      .filter(_ match {
          case Success(pr) => true
          case Failure(pr) => false
      })
      .map(_.get)
  }
}

