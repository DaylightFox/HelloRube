public class LambdaHelloWorld {
    public static void main(String[] args) {
        "Hello, World!".chars().mapToObj(c -> (char) c).forEach(System.out::println);
    }
}