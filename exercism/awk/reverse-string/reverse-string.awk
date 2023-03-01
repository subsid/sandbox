BEGIN {FS="";result=""}
{
  for (i = NF; i > 0; i--) {
    result = result $i
  }
}
END {
  print result
}
