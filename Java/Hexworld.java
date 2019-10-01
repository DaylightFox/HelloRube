import java.math.BigInteger;

public class Hexworld {
    public static void main(String[] args){
        String hexStr = "48656c6c6f20576f726c64";
        String ASCII = hexConverter(hexStr);
        System.out.println(ASCII);
    }
    private static String hexConverter(String hexStr) {
        StringBuilder output = new StringBuilder("");
         
        for (int i = 0; i < hexStr.length(); i += 2) {
            String str = hexStr.substring(i, i + 2);
            output.append((char) Integer.parseInt(str, 16));
        }
         
        return output.toString();
    }
}
