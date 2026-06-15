
import java.math.BigInteger;

public class PrimeFields {

    public static void main(String[] args) {
        int fields = 0;
        for (int pi = 100; pi <= 400; ++pi) {
            final var x = BigInteger.ONE.shiftLeft(pi);
            for (int theta = 1; theta < 20; theta += 2) {
                final var thetaBigInt = BigInteger.valueOf(theta);
                final var candidate = x.subtract(thetaBigInt);
                if (candidate.isProbablePrime(100)) {
                    System.out.println("\"" + pi + " " + theta + "\"");
                    fields += 1;
                    break;
                }
            }
        }
        System.out.println("Found " + fields + " fields.");
    }

}
