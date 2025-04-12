//static
public class SingletonCls {
    private static SingletonCls instance= new SingletonCls();
    private SingletonCls() {
    }
    public static SingletonCls getInstance() {
        return instance;
    }
    public static void main(String[] args) {
        Singleton3 singleton = Singleton3.getInstance();
        System.out.println(singleton);
        Singleton3 singleton1 = Singleton3.getInstance();
        System.out.println(singleton1);
    }
}

