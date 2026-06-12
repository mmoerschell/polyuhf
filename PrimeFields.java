
import java.math.BigInteger;

public class PrimeFields {

    public static void main(String[] args) {
        int fields = 0;
        for (int pi = 100; pi <= 400; ++pi) {
            final var x = BigInteger.ONE.shiftLeft(pi);
            for (int theta = 1; theta < 25; theta += 2) {
                final var candidate = x.subtract(BigInteger.valueOf(theta));
                if (candidate.isProbablePrime(80)) {
                    System.out.println(String.format("2^%d-%d", pi, theta));
                    fields += 1;
                    break;
                }
            }
        }
        System.out.println("Found " + fields + " fields.");
    }

}
