trait Default[F[_]] {
  def get[A]: F[A]
}

object Default {
  def apply[F[_]: Default] = implicitly(Default[F])

  implicit val listDefault: Default[List] =
    new Default[List] { def get[A]: List[A] = Nil }

  implicit val optionDefault: Default[Option] =
    new Default[Option] { def get[A]: Option[A] = None }
}

def getDefaults[F[_]]
