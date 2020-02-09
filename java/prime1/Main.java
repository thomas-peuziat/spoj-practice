// https://www.spoj.com/problems/PRIME1/
// https://dhruvpancholi.wordpress.com/2016/11/03/spoj-prime-generator-solution-in-java/
// A bit optimized for PRIME1, ~5-10% faster

package prime1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        InputReader in = new InputReader(System.in);
        SieveOfEratosthenes soe = new SieveOfEratosthenes(SieveOfEratosthenes.LIMIT);

        int T = in.nextInt();
        while (T-- != 0) {
            int m = in.nextInt();
            int n = in.nextInt();
            if (n < SieveOfEratosthenes.LIMIT) {
                for (int i = m; i <= n; i++) {
                    if (soe.isPrime(i)) {
                        System.out.println(i);
                    }
                }
            } else {

                // primes which are lesser than the square root of n, since the
                // max prime factor of n will be less than or equal to square root of n
                List<Integer> primes = soe.getPrimes((int) Math.sqrt(n));

                boolean[] a = new boolean[n - m + 1];
                for (int i = 0; i < a.length; i++) {
                    a[i] = true;
                }

                // Similar to sieve of eratosthenes, fill the boolean
                // array with the divisibility with prime factors
                for (int prime : primes) {
                    int div = m / prime;
                    if (div * prime == m) {
                        a[0] = false;
                    } else {
                        div += 1;
                    }
                    for (int i = div * prime; i <= n; i += prime) {
                        if (i >= m && i <= n) {
                            a[i - m] = false;
                        }

                    }
                }

                for (int i = 0; i < a.length; i++) {
                    if (a[i]) {
                        System.out.println(m + i);
                    }
                }
            }
            System.out.println();
        }
    }

    public static class SieveOfEratosthenes {

        public static final int LIMIT = 10000000;

        private boolean[] a;

        public SieveOfEratosthenes(int N) {
            a = new boolean[N + 1];
            for (int i = 0; i < N; i++) {
                a[i] = true;
            }
            a[0] = false;
            a[1] = false;

            int root = (int) Math.sqrt(N);
            for (int i = 2; i <= root; i++) {
                for (int j = i * i; j <= N; j += i) {
                    a[j] = false;
                }
            }
        }

        public boolean isPrime(int n) {
            return a[n];
        }

        public List<Integer> getPrimes() {
            List<Integer> list = new ArrayList<Integer>();
            for (int i = 1; i < a.length; i++) {
                if (a[i]) {
                    list.add(i);
                }
            }
            return list;
        }

        public List<Integer> getPrimes(int n) {
            List<Integer> list = new ArrayList<Integer>();
            for (int i = 1; i <= n; i++) {
                if (a[i]) {
                    list.add(i);
                }
            }
            return list;
        }
    }

    public static class InputReader {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
}