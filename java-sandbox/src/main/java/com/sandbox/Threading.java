package com.sandbox;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.util.concurrent.*;

import static org.junit.Assert.*;

// https://www.baeldung.com/thread-pool-java-and-guava
public class Threading {
    class Counter {
        int count = 0;

        public int getCount() {
            return count;
        }

        public void increment() {
            count++;
        }
    }

    private static void singleThreadExecutor() {
        Executor executor = Executors.newSingleThreadExecutor();
        // Takes a runnable
        executor.execute(() -> System.out.println("Hello world"));
    }

    private static void fixedPoolExecutor() throws ExecutionException, InterruptedException {
        ExecutorService executorService = Executors.newFixedThreadPool(10);
        executorService.submit(() -> System.out.println("Hello world runnable"));
        Future<String> f = executorService.submit(() -> "Hello world callable");
        System.out.println("Future done? " + f.isDone());
        String result = f.get();
        System.out.println("Got result " + result);
        executorService.shutdown();
    }

    private static void threadPoolExecutor() {
        // FixedThreadPool creates a ThreadPoolExecutor with maxPoolSize = corePoolSize
        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(2);
        executor.submit(() -> {
            Thread.sleep(1000);
            System.out.println("Callable job");
            return null;
        });
        executor.submit(() -> {
            try {
                Thread.sleep(1000);
                System.out.println("Runnable job done");
            } catch (InterruptedException e) {
                System.out.println("Interrupted exception");
                e.printStackTrace();
                throw new UncheckedIOException(new IOException());
            }
        });
        executor.submit(() -> System.out.println("Third job"));
        executor.submit(() -> System.out.println("Fourth job"));
        assertEquals(2, executor.getPoolSize());
        assertEquals(2, executor.getQueue().size());
        executor.shutdown();
            }


    public static void main(String[] args) throws ExecutionException, InterruptedException {
//        fixedPoolExecutor();
        threadPoolExecutor();
//        forkJoinPoolExecutor();
    }

    private static void forkJoinPoolExecutor() {
    }
}
