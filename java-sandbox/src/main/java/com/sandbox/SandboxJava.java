package com.sandbox;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Stream;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

class Doc {
    private final String title;
    private final String id;

    public String getTitle() {
        return title;
    }

    public String getId() {
        return id;
    }

    public Doc(JSONObject doc) {
        title = (String) doc.get("title");
        id = (String) doc.get("id");
    }

    public String toString() {
        return String.format("%s (%s)", this.title, this.id);
    }
}

class Result  implements Comparable<Result>{
    private final Long score;
    private final Doc doc;

    Result(Long score, Doc doc) {
        this.score = score;
        this.doc = doc;
    }

    @Override
    public int compareTo(Result o) {
        // Sort descending
        return (int) (o.score - this.score);
    }

    @Override
    public String toString() {
        return String.format("Score: %d, Doc: %s", score, doc.toString());
    }
}

interface BaseMatcher {
    void indexFromPath(String docPath);
    List<Result> match(String query, Integer limit);
}

class Matcher implements BaseMatcher {
  private final HashMap<String, Doc> documents;

  public Matcher() {
      this.documents = new HashMap<>();
  }

  public void indexFromPath(String docPath) {
    JSONParser parser = new JSONParser();
    try (Stream<String> stream = Files.lines(Paths.get(docPath))) {
      stream
              .forEach(
                      (line) -> {
                        try {
                          Doc doc = new Doc((JSONObject) parser.parse(line));
                          this.documents.put(doc.getId(), doc);
                        } catch (ParseException e) {
                          e.printStackTrace();
                        }
                      });
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public List<Result> match(String query, Integer limit) {
      ArrayList<Result> results = new ArrayList();
      String[] terms = query.split(" ");
    documents.forEach(
        (doc_id, doc) -> {
          long termMatchCt = Arrays.stream(terms).filter((t) -> doc.getTitle().contains(t)).count();
          if (termMatchCt > 0) {
            results.add(new Result(termMatchCt, doc));
          }
        });

      Collections.sort(results);
      return results.subList(0, Math.min(results.size(), limit - 1));
  }
}
class SandboxJava {

  public static void main(String[] args) {
    int limit = 10;
    Matcher m = new Matcher();
    m.indexFromPath("/home/sid/workspace/scripts/listings.docs");
    List<String> queries = new ArrayList();
    //    queries.add("Something related to harry potter and wine");
    //    queries.add("Harry Potter Wine Glass");
    //    queries.add("Gryffindor Hogwarts");

    for (String query : queries) {
      List<Result> result = m.match(query, limit);
      System.out.println("*********************");
      System.out.println(query);
      result.forEach(
          (r) -> {
            System.out.println(r);
          });
      System.out.println("*********************");
    }
  }
}

