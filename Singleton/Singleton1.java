
//Synchronized Method
public class Singleton1 {
    private static Singleton1 instance;
    private Singleton1() {}
    public static synchronized Singleton1 getInstance() {
        if (instance == null) {
            instance = new Singleton1();
        }
        return instance;
    }
    public static void main(String[] args) {
        Singleton1 singleton = Singleton1.getInstance();
        System.out.println(singleton);
        Singleton1 singleton1 = Singleton1.getInstance();
        System.out.println(singleton1);
    }
}
