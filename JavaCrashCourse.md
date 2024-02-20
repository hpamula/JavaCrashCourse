# Wykład 1.

```java
public class Main {
    public static void main(String[] args) {
        
    }
}
```
### JDK, JRE
JDK (Java Development Kit) zawiera JRE (Java Runtime Environment), który jest potrzebny do uruchamiania programów w Java. Właścicielem języka jest firma Oracle.

Cały kod w Java jest wewnątrz klas.
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```
System.out.println
- System to klasa
- out to atrybut klasy, obiekt
- println to metoda przyjmująca jako argument String
kompilujemy poleceniem `javac <nazwa pliku>`
żeby uruchomić JVM piszemy `java <nazwa klasy>`

### Prymitywne typy danych
Prymitywne typy danych:
- byte (8-bit), short (16-bit), int (32-bit), long (64-bit)
- float (32-bit), double (64-bit)
- boolean (1-bit)
- char (16-bit) - znak w unicode, np. `\u<4 znaki>`
Obiektowe typy danych:
- String, PrintStream, wszystko inne

String to obiekt
out jest typu PrintStream
### If, switch
```java
public class Main {
    public static void main(String[] args) {
        System.out.println(_if(Integer.parseInt(args[0])));
        _switch(Integer.parseInt(args[0]));
    }
    static int _if(int a) {
        if(a > 0) {
            return 1;
        } else {
            return -1;
        }
    }
    static void _switch(int a) {
        // switch(<zmienna typu prymitywnego>)
        switch(a) {
            case 1: System.out.println(100);
                break;
            case 2: System.out.println(200);
            // default nieobowiązkowe, wykonuje się jeśli żaden z warunków nie jest prawdziwy
            default: a++; System.out.println(a);
        }
    }
}
```
### For, while, do...while
```java
import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        _for(args);
        
        String s = "Ala";
        while(s.length() < 20)
            s = " " + s;
        System.out.println(s);

        do {
            String ww = "3";
        } while (ww != null);
        System.out.println(ww);
    }
    static void _for(String[] args) {
        for(int i = 0; i < args.length; i++)
            System.out.printf(Locale.US, "%.2f\n", Double.parseDouble(args[i]));
    }
}
```
W Java są tylko referencje
stringi porównujemy używając `<String1>.equals(<String2>)`
`break;`
`continue;`

```java
public class SquareRoot {
    public static final double precision = 1.0e-5;
    public static double calculateSquareRoot(double x) {
        double guess = 1.0;
        do {
            guess = (guess + x/guess)/2.0;
            System.out.println(guess);
        } while((guess*guess/x < 1.0-precision) || (guess*guess/x > 1.0+precision));
        return guess;
    }
    public static void main(String[] args) {
        if(args.length < 1)
            System.out.println("Brak argumentu");
        else
            System.out.println(calculateSquareRoot(Double.parseDouble(args[0])));
    }
}
```
```java
public class ParabolaRoots {
    public static double[] getRoots(double a, double b, double c) {
        double[] roots = new double[3];
        double delta = b*b-4*a*c;
        if(delta < 0) {
            roots[0] = 0;
        } else {
            roots[0] = (delta == 0)?1:2;
            roots[1] = (-b+Math.sqrt(delta))/(2*a);
            roots[2] = (-b-Math.sqrt(delta))/(2*a);
        }
        return roots;
    }
    public static void main(String[] args) {
        System.out.println(args.length);
        for(int i = 0; i < args.length; i++)
            System.out.println(args[i]);
        double a = Double.parseDouble(args[0]);
        if(a == 0)
            System.out.println("Nieprawid\u0142owe dane");
        double b = Double.parseDouble(args[1]);
        double c = Double.parseDouble(args[2]);
        double[] results = getRoots(a, b, c);
        String[] sa = {"Liczba rzeczywistych pierwiastk\u00f3w: ", "x1 = ", "x2 = "};
        for(int i = 0; i < results[0]+1; i++)
            System.out.println(sa[i] + results[i]);
    }
}
```
# Wykład 2
### Pakiety, dostępność
```java
//package pakiet.podpakiet;
public class Klasa {
    public int publiczny;
    protected int chroniony; //dostępny tylko w danej klasie, klasach potomnych i z tego samego pakietu
    int zwykly; //dostępny tylko w danej klasie i z tego samego pakietu, czyli dokładnie w tym samym folderze (w podfolderach już nie)
    private int prywatny; //dostępny tylko w danej klasie

    private Klasa() {
        //konstruktor nie musi być publiczny
    }
    public Klasa(int a, int b, int c, int d) {
        this.publiczny = a;
        this.prywatny = b;
        this.chroniony = c;
        this.zwykly = d;
    }
    public static void main(String args[]) {
        System.out.println("Main 1");
        Klasa k = new Klasa();
        System.out.println(k.publiczny);
    }
}
public class Test {
    public static void main(String args[]) {
        System.out.println("Test");
        Klasa k = new Klasa(1, 2, 3, 4);
        System.out.println(k.chroniony);
    }
}
```
Uruchomienie klasy z podfolderu
`java pakiet.podpakiet.Klasa`
`Klasa.class` musi być w `./pakiet/podpakiet/`

Użycie klasy z innego pakietu
`import pakiet.podpakiet.Klasa;`
`import pakiet.podpakiet.*;`

Konwencja jest taka, że w Java wszystko z małej litery, a tylko klasy z dużej litery.
Nazwy pakietów - odwrotne nazwy domenowe dla unikalności, np.
pl.edu.uj.fais.java.wyklad2
### Static, abstract, record
```java
public class OrderTest {
    static {
        //wszystko w tym bloku wykonuje się, gdy JVM załaduje klasę
        System.out.println("static");
    }
    public OrderTest() {
        System.out.println("constructor");
    }
    public static void main(String[] args) {
        System.out.println("main: begin");
        OrderTest o;
        System.out.println("main: middle");
        o = new OrderTest();
        System.out.println("main: end");
    }
}
```
Klasa abstrakcyjna, to zwykle klasa, której co najmniej jedna z metod jest abstrakcyjna. Nie można bezpośrednio tworzyć instancji klasy abstrakcyjnej.
Klasa może mieć tylko jednego bezpośredniego rodzica.
Jeśli klasa nie posiada rodzica, to dziedziczy automatycznie po Object (`java.lang.Object`)
Pakiet `java.lang` jest zawsze domyślnie importowany.
Interfejs ma wszystkie metody tylko zadeklarowane, bez żadnej implementacji. Interfejs może mieć tylko atrybuty statyczne.
Publiczny interfejs musi być zadeklarowany w pliku o nazwie takiej jak interfejs.
```java
public record RecordExample(int id,
                           String title,
                           String describtion,
                           double price) { }
public class Test {
    public static void main(String[] args) {
        RecordExample re = new RecordExample(1, "tytul", "opis", 123.34);
        System.out.println(re.title());
    }
}
```
Nie można zmieniać atrybutów klasy (jak w klasie z modyfikatorem `final` przed nazwą). Rekord może mieć dodatkowe atrybuty i metody w nawiasach klamrowych.
### Javadoc
```java
import java.io.IOException;

/**
 * Klasa umożliwiająca zgadywanie liczby, którą wylosował komputer
 * @author Kubuś Puchatek
 */
public class TryAndCheck {
    private int number;
    /**
     * konstruktor, w nim odbywa się losowanie liczby
     */
     public TryAndCheck() {
         // typy prymitywne możemy rzutować w ten sposób
         this.number = (int)(Math.random()*10);
         // System.out.println(this.number);
     }
     /*
     sprawdza, czy podana wartość ...
     @param iv
     @return -1, gdy iv jest mniejsza, 1, gdy większa, 0 gdy równa
     */
     public byte check(int iv) {
         if(iv < this.number) return -1;
         if(iv > this.number) return +1;
         return 0;
     }
     /*
     metoda uruchamiana automatycznie. Przeprowadza rozgrywkę
     @param args nieobslugiwane
     @throws IOException w przypadku niepoprawnych danych
     */
     public static void main(String[] args) throws IOException {
         TryAndCheck play = new TryAndCheck();
         int res;
         char c;
         do {
             c = (char)System.in.read(); // odczytujemy znak
             System.out.println("Wczytano: " + c);
             res = play.check(Integer.valueOf(Character.toString(c))); // a co jeśli (int)?
             //c = (char)
             c = (char)System.in.read(); // odczytujemy enter
             c = (char)System.in.read(); // odczytujemy drugi enter, bo Windows
             if(res < 0)
                 System.out.println("Za ma\u0142o");
             if(res > 0)
                 System.out.println("Za du\u017co");
         } while(res != 0);
         System.out.println("Gratulacje!");
     }
}
```
Generowanie dokumentacji `javadoc TryAndCheck.java`
# Wykład 3
### Throwable
Klasa Throwable ma dwie klasy potomne
1. `Exception` - na nie możemy reagować w kodzie
    - `RuntimeException` - ich nie musimy obsługiwać
        - `NullPointerException`
        - `IndexOutOfBoundsException`
    - wszystkie pozostałe musimy obsługiwać
1. `Error` - program jest przerywany i nie jest możliwa jego kontynuacja
    - `OutOfMemoryError`

### try catch finally, throws
Wyjątek obsługujemy albo przez
`try{}catch(){}catch(){}catch(){}finally{}`
albo przekazać wyjątek wyżej przez
`<nagłówek metody> throws ..., ..., ...`
Finally się wykonuje zawsze poza System.exit wykonanym wcześniej
Można łączyć wyjątki
`catch(FileNotFoundException | NullPointerException ex){}`
```java
public class Main {
    public static void main(String[] args) {
        String s = null;
        try {
            s.split(" ");
        } catch(NullPointerException ex) {
            System.out.println("NullPointerException");
        } catch(Exception ex) {
            System.out.println("Exception");
        } finally {
            System.out.println("Finally");
        }
    }
}
```
Możemy definiować własne wyjątki
`public class MyException extends Exception`
i rzucamy je słówkiem `throw`
### Kolekcje
Implementacje najpopularniejszych kolekcji w Java jest w `java.util`
Każda kolekcji implementuje `java.util.Collection`
Przykładowe klasy rozszerzające
- `ArrayList`
- `HashSet`
- `LinkedList`
- `Stack`
- `Vector`
- `PriorityQueue`
- `TreeSet`
- ...
Przykładowe interfejsy rozszerzające
- `List`
- `Set`
- `SortedSet`
- `Queue`
- `Deque`
- ...
```java
import java.util.Vector;
import java.util.Iterator;
import java.util.Enumeration;

public class Main {
    public static void main(String[] args) {
        Vector v = new Vector();
        v.add("Ala");
        v.add(true);
        v.add(128.5);
        v.add("Ola");
        for(int i = 0; i < v.size(); i++) {
            Object o = v.get(i);
            System.out.println(o.getClass().getCanonicalName() + "\t" + o);
        }
        for(Enumeration e = v.elements(); e.hasMoreElements();) {
            Object o = e.nextElement();
            System.out.println(o.getClass().getCanonicalName() + "\t" + o);
        }
        for(Iterator e = v.iterator(); e.hasNext();) {
            Object o = e.next();
            System.out.println(o.getClass().getCanonicalName() + "\t" + o);
        }
        for(Object o : v) {
            System.out.println(o.getClass().getCanonicalName() + "\t" + o);
        }
    }
}
```
Możemy określić typ, żeby nie trzeba było rzutować w przyszłości
`Vector<String> v = new Vector<>();`
Kopię robimy używając `.clone();` np.
`v2 = (Vector)v.clone();`
bo `.clone()` zwraca `Object`
Operacja na `Vector` są synchronizowane, a na `ArrayList` nie są i dzięki temu ta druga jest szybsza
```java
import java.util.Hashtable;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import java.awt.Graphics;
import java.awt.Dimension;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Hashtable<String, BufferedImage> ht = new Hashtable<>();
        for(File f : new File(System.getProperty("user.dir")).listFiles()) {
            if(f.getName().endsWith(".jpg")) {
                ht.put(f.getName(), ImageIO.read(f));
            }
        }
        final BufferedImage bi = ht.get("logo.jpg");
        JFrame frame = new JFrame() {
            public void paint(Graphics g) {
                super.paint(g);
                g.drawImage(bi, 0, 0, null);
            }
        };
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setPreferredSize(new Dimension(bi.getWidth(), bi.getHeight()));
        frame.pack();
        frame.setVisible(true);
    }
}
```
`Hashtable` daje nam elementy w czasie O(1)
Jest `synchronized` w przeciwieństwie do `Hashmap`
Pozwala na klucze i wartości `null` w przeciwieństwie do `Hashmap`
```java
public class Properties extends Hashtable<Object, Object>;
public synchronized Object setProperty(String key, String value);
public String getProperty(String key);
```
```java
import java.util.Properties;

public class Main {
    public static void main(String[] args) {
        Properties p;
        p = System.getProperties();
        p.list(System.out);
    }
}
```
```java
import java.util.Properties;
import java.io.FileOutputStream;
import java.io.StringReader;
import java.io.IOException;
import java.io.FileNotFoundException;

public class Main {
    public static void main(String[] args) throws IOException, FileNotFoundException {
        String data = """
            # analizowany plik w formacie gif, png, jpg
            image = obrazek.png
            output=res.png
            # inne ustawienia
            moversCount=500
            stepSize = 1
            ballRadius=1""";
        Properties p = new Properties();
        p.load(new StringReader(data));
        p.storeToXML(new FileOutputStream("ustawienia.xml"), "");
    }
}
```
Klasy `Collections` oraz `Arrays` zawierają przydatne metody statyczne, np.
```java
public static <T extends Comparable<? super T>> void sort(List<T> list)
```
# Wykład 4
### Generyczne klasy, raw
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Ala");
        String s = list.get(0);
        System.out.println(s);
    }
}
```
Konwencje
- T -typ
- K - klucz
- V - wartość
- E - element (np. kolekcji)
- N - liczba

```java
public class Box<T> {
    private T t;
    public void set(T t) {
        this.t = t;
    }
    public T get() {
        return t;
    }
    public static void main(String[] args) {
        Box<String> typedBox = new Box<String>();
        // typedBox.set("hi");
        Box rawBox = new Box();
        rawBox = typedBox;
        rawBox.set(8);
        System.out.println(rawBox.get());
        // a na wykładzie powiedział, że to nie zadziała i będzie Runtime Exception
    }
}
```
### Generyczne metody
Możemy mieć niegeneryczną klasę, która posiada metody generyczne
```java
public interface Pair<K, V> {
    public K getKey();
    public V getValue();
}
public class OrderedPair<K, V> implements Pair<K, V> {
    private K key;
    private V value;
    public OrderedPair(K key, V value) {
        this.key = key;
        this.value = value;
    }
    public K getKey() {
        return key;
    }
    public V getValue() {
        return value;
    }
    public static void main(String[] args) {
        Pair<String, Integer> p = new OrderedPair<>("Even", 8);
    }
}
public class Util {
    public static <K, V> boolean equals(Pair<K, V> p1, Pair<K, V> p2) {
        return p1.getKey().equals(p2.getKey()) && p1.getValue().equals(p2.getValue());
    }
    public static void main(String[] args) {
        Pair<String, Integer> p = new OrderedPair<>("Even", 8);
        Pair<String, Integer> p2 = new OrderedPair<>("Even", 8);
        Pair<String, Integer> p3 = new OrderedPair<>("Even", 10);
        System.out.println(Util.<String, Integer>equals(p, p2));
        System.out.println(Util.equals(p, p2));
        System.out.println(Util.equals(p, p3));
    }
}
```
### Generyczne extends, super
```java
public class Box<T> {
    private T t;
    public void set(T t) {
        this.t = t;
    }
    public <U extends Number> void inspect(U u) {
        System.out.println(t.getClass().getName());
        System.out.println(u.getClass().getName());
    }
    public static void main(String[] args) {
        Box<Integer> integerBox = new Box<>();
        integerBox.set(10);
        integerBox.inspect(1.1f);
        // integerBox.inspect("error");
    }
}
```
### Extends Interface/s
```java
public class NaturalNumber<T extends Integer>
<T extends C & I1 & I2>
// C to klasa, bo można rozszerzać tylko jedną klasę, a I1, I2 to interfejsy
```
```java
public class Main {
    public static <T extends Comparable<T>> int countGreaterThan(T[] anArray, T elem) {
        int count = 0;
        for(T e : anArray) {
            if(e.compareTo(elem) > 0)
                count++;
        }
        return count;
    }
    public static void main(String[] args) {
        System.out.println(countGreaterThan(new Integer[]{0, 1, 2, 3}, 1));
        System.out.println(countGreaterThan(new String[]{"0", "1", "2", "3"}, "1"));
    }
}
```
### `Integer extends Number` =/> `Box<Integer> extends Box<Number>`
```java
public class Box<T> {
    private T t;
    public void set(T t) {
        this.t = t;
    }
    public T get() {
        return t;
    }
    public static void main(String[] args) {
        Box<String> typedBox = new Box<String>();
        // typedBox.set("hi");
        Box rawBox = new Box();
        rawBox = typedBox;
        rawBox.set(8);
        System.out.println(rawBox.get());
        // a na wykładzie powiedział, że to nie zadziała i będzie Runtime Exception
        System.out.println("=====================");
        Box<Integer> boxInteger = new Box<>();
        Box<Number> boxNumber = new Box<>();
        Box box = new Box();
        // box = boxInteger;
        // box = boxNumber;
        boxNumber = box;
        boxInteger = box;
        // boxInteger = boxNumber; // błąd
        // boxNumber = boxInteger; // błąd
        boxInteger.set(6);
        box.set(5.5);
        System.out.println(box.get());
        System.out.println(boxInteger.get());
        // dlaczego to działa? Box<Integer> teraz przechowuje double?
    }
}
```
### ? - symbol wieloznaczny
```java
import java.util.*;

public class Main {
    public static <E> void function(List<E> list) {
        for(Object o : list) {
            System.out.println(o);
            System.out.println(o.getClass());
        }
    }
    public static void main(String[] args) {
        List rawList = new ArrayList();
        rawList.add(12);
        List l = new Stack();
        l.add(new PriorityQueue());
        List<?> wild = l;
        rawList.add(wild);
        rawList.add(new ArrayList<Thread>());
        rawList.add("asda");
        function(rawList);
    }
}
```
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static <T extends Number> double sumOfList(List<T> list) //czym to się różni o d tego niżej
    // public static double sumOfList(List<? extends Number> list)
    {
        double s = 0.0;
        for(Number n : list)
            s += n.doubleValue();
        return s;
    }
    public static void main(String[] args) {
        System.out.println(sumOfList(List.of(1, 2.4, 3.1f)));
        List l = new ArrayList();
        l.add(1);
        l.add(2.4);
        l.add(3.1f);
        System.out.println(sumOfList(l));
        List<? extends Number> wild = new ArrayList();
        // wild.add(1); // compile error
        wild.add(null);
        wild = l;
        System.out.println(sumOfList(l));
        System.out.println(sumOfList(wild));
        // List<T extends Object> sa; // compile error
    }
}
```
`?` to ograniczenie od góry
```java
import java.util.List;
import java.util.Stack;

public class Main {
    // public static void printList(List<?> list)
    // to jedno poniżej chyba  miało nie działać, ale tu działa
    public static <T> void printList(List<T> list)
    // public static void printList(List<Object> list) // nie działa, chyba, że dla List.of, bo List<String> nie jest podklasą List<Object>
    {
        for(Object elem : list)
            System.out.println(elem + " ");
        System.out.println();
    }
    public static void main(String[] args) {
        // printList(List.of("asda", 2.4, 3.1f));
        List<String> l = new Stack<>();
        l.add("131312");
        l.add("adsa");
        printList(l);
        List<Integer> k = new Stack<>();
        k.add(1);
        k.add(100);
        printList(k);
        List<List<List<Integer>>> r = new Stack<>();
        List<List<Integer>> n = new Stack<>();
        printList(n);
        k.add(130);
        n.add(k);
        r.add(n);
        printList(r);
    }
}
```
```java
import java.util.ArrayList;
import java.util.List;

class WildcardError {
    public static void doSomething(List<?> l) {
        // l.set(0, l.get(0)); // błąd kompilacji
        // System.out.println(l.get(0));
        System.out.println(l);
    }
    public static <T> void doSomethingBetter(List<T> l) {
        // l.set(0, l.get(0));
        // System.out.println(l.get(0));
        System.out.println(l);
    }
}
public class Main {
    public static void main(String[] args) {
        ArrayList<String> a = new ArrayList<>();
        a.add("asda");
        ArrayList b = new ArrayList();
        WildcardError.doSomething(a);
        WildcardError.doSomething(b);
        WildcardError.doSomethingBetter(a);
        WildcardError.doSomethingBetter(b);
        List<Integer> li = new ArrayList<Integer>();
        List lw = new ArrayList();
        List<? extends Number> ln = lw;
        WildcardError.doSomething(ln);
        WildcardError.doSomethingBetter(ln);
    }
}
```
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> li = new ArrayList<Integer>();
        List<? extends Number> ln = li;
        ln.add(new Integer(34)); // błąd kompilacji
    }
}
```
`Integer` nie jest `Number`
### Metody pomostowe
```java
public class Box<T> {
    private T t;
    public void set(T t) {this.t = t;}
}
//po kompilacja staje się:
// public class B ox {
//     private Object t;
//     public void set(Object t) {this.t = t;}
// }
public class MyBox extends Box<String> {
// nie chcemy mieć dwóch metod w MyBox, tylko tę jedną, a wywoła się metoda dla Object (nawet jeśli będzie on String'iem)
// dlatego kompilator dodaje metodę pomostową:
// public void set(Object data) {
//     set((String) data);
// }
    public void set(String s) {
        System.out.println(s);
    }
}
public class Main {
    public static void main(String[] args) {
        MyBox m = new MyBox();
        m.set("asda");
    }
}
```
# Wykład 5
`IOException` to wyjątek najwyższy wejścia/wyjścia
```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class CopyBytes {
    public static void main(String[] args) throws IOException {
        FileInputStream in = null;
        FileOutputStream out = null;
        try {
            in = new FileInputStream("input.java");
            out = new FileOutputStream("output.txt");
            int c;
            
            while((c = in.read()) != -1) {
                out.write(c);
            }
        } finally {
            if(in != null) {in.close();}
            if(out != null) {out.close();}
        }
    }
}

// public record input
// adasd
// asda
// sdadasdasd23 23
```
```java
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class CopyCharacters {
    public static void main(String[] args) throws IOException {
        FileReader in = null;
        FileWriter out = null;
        try {
            in = new FileReader("input.java");
            out = new FileWriter("output.txt");
            int c;
            
            while((c = in.read()) != -1) {
                out.write(c);
            }
        } finally {
            if(in != null) {in.close();}
            if(out != null) {out.close();}
        }
    }
}

// public record input
// qweqe222
// ;';a's;asda
// sdadasdasd23 23
```
```java
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.IOException;

public class CopyLines {
    public static void main(String[] args) throws IOException {
        BufferedReader in = null;
        PrintWriter out = null;
        try {
            in = new BufferedReader(new FileReader("input.java"));
            out = new PrintWriter(new FileWriter("output.txt"));
            String l;
            while((l = in.readLine()) != null) {
                out.println(l);
            }
        } finally {
            if(in != null) {in.close();}
            if(out != null) {out.close();}
        }
    }
}

// public record input
// []qweqe222
// ;';a's;asda
// sdadasdasd23 23
```
```java
import java.io.*;
import java.util.Scanner;

public class ScanXan {
    public static void main(String[] args) throws IOException {
        Scanner s = null; // domyślnym tokenem jest Whitespace
        try {
            s = new Scanner(new BufferedReader(new FileReader("input.java")));
            s = new Scanner(new FileReader("input.java"));
            // s = new Scanner(System.in);
            s.useDelimiter(",\\s*");
            while(s.hasNext()) {
                System.out.println(s.next());
            }
        } finally {
            if(s != null) {s.close();}
        }
    }
}

// public record input
// 1231,312, 23, 23, 2 2 
// []qweqe222
// ;';a's;asda
// sdadasdasd23 23
```
### Formatowanie
```java
import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        double d = 2.0;
        double s = Math.sqrt(2.0);
        System.out.println("Pierwiastek z " + d + " to " + s);
        System.out.format("Pierwiastek z %f to %.4f\n", d, s);
        System.out.format(Locale.US, "Pierwiastek z %f to %.4f\n", d, s);
        System.out.printf(Locale.US, "Pierwiastek z %f to %.4f\n", d, s);
    }
}
```
### Metody wieloargumentowe
```java
public class Main {
    public static void multiint(int... ints) {
    // mogą być też zwykłe argumenty, ale tylko najpierw normalne, a na końcu tablicowy
        for(int i = 0; i < ints.length; i++)
            System.out.println(ints[i]);
        System.out.println();
        for(int i : ints)
            System.out.println(i);
    }
    public static void main(String[] args) {
        multiint(123, 34, 65, 76, 44, 11, 0);
        multiint();
        multiint(12, 28);
    }
}
```
### Zasoby i lokalizacja
```java
import java.util.Locale;
import java.util.ResourceBundle;

public class LocalizationExample {
    public static void main(String[] args) {
        //to jaki plik się linijkę niżej wczyta zależy od ustawień regionalnych (nie tylko język, ale też rodzaj języka, czy rodzaj OS)
        ResourceBundle rb = ResourceBundle.getBundle("resources");
        for(String key : rb.keySet())
            System.out.println(key + ": " + rb.getString(key));
    }
}

// resources_pl.properties
```
### Class Loader
```java
public class Main {
    public static void main(String[] args) {
        class NetworkClassLoader extends ClassLoader {
            String host;
            int port;
            
            public Class findClass(String name) {
                byte[] b = loadClassData(name);
                return defineClass(name, b, 0, b.length);
            }
            private byte[] loadClassData(String name) {
                // wczytywanie bytecode'u klasy z określonej lokalizacji sieciowe
            }
        }
    }
}
```
### Strumienie binarne
```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        DataOutputStream dos = new DataOutputStream(System.out);
        dos.writeDouble(123.12);
        dos.writeUTF("Grzegrzó\u0142ka");
        dos.writeInt(12345);
        dos.close();
        System.out.println("=====================");
        ObjectOutputStream oos = new ObjectOutputStream(System.out);
        oos.writeObject("Grzegrzó\u0142ka");
        oos.close();
    }
}
```
Żeby się dało serializować, to klasa musi implementować `Serializable`
`writeObject` i `readObject` możemy wtedy napisać, które Java wykorzysta
### Serializacja
```java
import java.io.*;

public class SerializationTest implements Serializable {
    public int id;
    public String name;

    public SerializationTest(int i, String s) {
        this.id = i;
        this.name = s;
    }
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        SerializationTest st1 = new SerializationTest(7, "Ala");
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("output_object"));
        oos.writeObject(st1);
        oos.close();
        SerializationTest st2;
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("output_object"));
        st2 = (SerializationTest)ois.readObject();
        ois.close();
        System.out.println(st2.id + "\t" + st2.name);
    }
}
```
### Strumienie kompresujące
```java
import java.util.zip.*;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException, FileNotFoundException {
        Scanner sc = new Scanner(System.in);
        GZIPOutputStream gos = new GZIPOutputStream(new FileOutputStream(args[0]));
        while(sc.hasNext()) {
            String s = sc.nextLine() + "\n";
            gos.write(s.getBytes());
        }
        sc.close();
        gos.close();
    }
}
```
`GZIPOutputStream` tylko kompresuje dane, a zapisuje je `FileOutputStream`, którego dostał w konstruktorze
```java
import java.util.zip.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException, FileNotFoundException {
        ZipOutputStream zos = new ZipOutputStream(new FileOutputStream("plik.zip"));
        for(int i = 0; i < 50; i++) {
            ZipEntry ze = new ZipEntry("plik" + i);
            zos.putNextEntry(ze);
            for(int j = 0; j < 1000; j++) {
                zos.write("Ala ma kota".getBytes());
            }
            zos.closeEntry();
        }
        zos.close();
    }
}
```
### JAR
`jar cf archiwum.jar klasa1.class klasa2.class`
`c` - tworzenie pliku
`f` - nazwa pliku
`m` - dodanie pliku manifest
`C` - zmiana katalogu, np. `ImageAudio.jar -C images * -C audio *`
W katalogu `META-INF` jest plik `MANIFEST.MF`, a w nim
`Main-Class: <ścieżka do klasy, od której zaczyna się uruchamianie>`
Uruchomienie jar:
`java -jar archiwum.jar`
# Wykład 6
### Tworzenie procesów
Program w Java jest uruchamiany w pojedynczego procesu
Wątki są uruchamiane na wspólnych danych
```java
import java.io.*;

public class processExample {
    public static void main(String[] args) {
        try {
            String s;
            Process ps = Runtime.getRuntime().exec("ls -l");
            BufferedReader bri = new BufferedReader(new InputStreamReader(ps.getInputStream())); // stream output
                BufferedReader bre = new BufferedReader(new InputStreamReader(ps.getErrorStream()));
            while((s = bri.readLine()) != null)
                System.out.println(s);
            bri.close();
            while((s = bre.readLine()) != null)
                System.out.println(s);
            bre.close();
            ps.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Gotowe");
    }
}
```
```java
import java.io.*;

public class processExample {
    public static void main(String[] args) {
        ProcessBuilder builder = new ProcessBuilder("ls -l");
        builder.directory(new File("."));
        builder.redirectErrorStream(true);
        builder.redirectOutput(ProcessBuilder.Redirect.INHERIT);
        Process ps;
        try {
            ps = builder.start();
            ps.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Gotowe");
    }
}
```
### Wątki
Wątki tworzymy przez rozszerzenia klasy `Thread` lub implementację `Runnable`
```java
public class HelloThread extends Thread {
    public void run() {
        System.out.println("Witam z wątku");
    }
    public static void main(String[] args) {
        Thread t = new HelloThread();
        t.start();
        // t.run(); // to nie tworzy nowego wątku
        System.out.println("Witam z programu");
    }
}
```
```java
public class HelloThread implements Runnable {
    public void run() {
        System.out.println("Witam z wątku");
    }
    public static void main(String[] args) {
        Thread t = new Thread(new HelloThread());
        t.start();
        // t.run(); // to nie tworzy nowego wątku
        System.out.println("Witam z programu");
    }
}
```
```java
public class HelloThread {
    public static void main(String[] args) {
        Runnable task = new Runnable() {
                public void run() {
                System.out.println("Witam z wątku");
            }
        };
        Thread t = new Thread(task);
        t.start();
        System.out.println("Witam z programu");
    }
}
```
```java
public class HelloThread {
    public static void main(String[] args) {
        Thread t = new Thread(new Runnable() {
                public void run() {
                System.out.println("Witam z wątku");
            }
        });
        t.start();
        System.out.println("Witam z programu");
    }
}
```
```java
public class HelloThread {
    public static void main(String[] args) {
        new Thread(() -> {
                System.out.println("Witam z wątku");
            }).start();
        System.out.println("Witam z programu");
    }
}
```
### Wstrzymywanie wykonania
```java
public class InterruptExample implements Runnable {
    public void run() {
        try {
            Thread.sleep(2000); // wstrzymanie na 1 s
        } catch (InterruptedException e) {
            System.out.println("interrupted");
        }
    }
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(new InterruptExample());
        t.start();
        Thread.sleep(1000);
        System.out.println("budzenie");
        t.interrupt();
    }
}
```
### Join
```java
public class JoinExample implements Runnable {
    public void run() {
        try {
            Thread.sleep(2000); // wstrzymanie na 1 s
        } catch (InterruptedException e) {
            System.out.println("interrupted");
        }
        System.out.println("watek");
    }
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(new JoinExample());
        t.start();
        t.join();
        System.out.println("teraz ja");
    }
}
```
### Synchronized 
```java
public class Counter {
    private int c = 0;
    // jedna blokada dla wszystkich metod danej instancji
    public synchronized void increment() {c++;}
    public synchronized void decrement() {c--;}
    public synchronized int value() {return c;}
    public static void main(String[] args) {
        
    }
}
```
### Blokada drobnoziarnista
```java
public class FineGrainedLock {
    private long c1 = 0, c2 = 0;
    private Object lock1 = new Object();
    private Object lock2 = new Object();
    public void inc1() {
        synchronized(lock1) {c1++;}
    }
    public void inc2() {
        synchronized(lock2) {c2++;}
    }
    public static void main(String[] args) {
        
    }
}
```
### Operacje atomowe
Aby operacja dostępu (odczyt/zapis) była atomowa używamy `volatile`
```java
public class Main {
    private volatile long c1 = 0;
    public void inc1() {c1 += 5;} // uwaga, nieatomowe, bo to zwiększanie, a nie odczyt/zapis
    public static void main(String[] args) {
        
    }
}
```
### Zakleszczenie
```java
public class Deadlock {
    static class Worker {
        public String name;
        public Worker(String name) {this.name = name;}
        public synchronized void doWork(Worker w) {
            System.out.println(this.name + " pracuje z " + w.name);
            try {Thread.sleep(1000);}
            catch (InterruptedException e) {}
            w.release();
        }
        public synchronized void release() {
            System.out.println(this.name + " jest znowu gotowy");
        }
    }
    public static void main(String[] args) throws InterruptedException {
        final Worker w1 = new Worker("w1");
        final Worker w2 = new Worker("w2");
        Thread t = new Thread(() -> {w1.doWork(w2);});
        t.start();
        t.join(); // bez tego jest zakleszczenie
        new Thread(() -> {w2.doWork(w1);}).start();
    }
}
```
### Wait, notify
`wait` i `notify` są w klasie Object
```java
public class Main {
    private boolean available;
    public synchronized void consume() {
        while(!available) {
            try {wait();} // wstrzymuje działanie wątku i zwalnia blokadę
            catch (InterruptedException e) {}
        }
        System.out.println("Skonsumowane");
        available = false;
    }
    public synchronized void produce() {
        // doProduce();
        available = true;
        notifyAll(); // powiadamia (budzi) wszystkie czekające wątki, tu mogłoby być też samo notify()
    }
    public static void main(String[] args) {
        
    }
}
```
### ReentrantLock
```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockObjects {
    static class Worker {
        public Lock lock = new ReentrantLock();
        public String name;
        
        public Worker(String name) {this.name = name;}
        public boolean tryWorking(Worker w) {
            // próba założenia blokady
            boolean myLock = lock.tryLock();
            boolean wLock = w.lock.tryLock();
            // jak się nie uda, to obie zwalniamy
            if(!(myLock && wLock)) {
                if(myLock) lock.unlock();
                if(wLock) w.lock.unlock();
            }
            return myLock && wLock;
        }
        public synchronized void doWork(Worker w) {
            boolean done = false;
            while(!done) {
                if(tryWorking(w)) {
                    System.out.println(this.name + " pracuje z " + w.name);
                    try {Thread.sleep(1000);}
                    catch (InterruptedException e) {}
                    w.release();
                    this.lock.unlock();
                    done = true;
                } else {
                    System.out.println(this.name + ": jestem zajety, wiec czekam");
                    try {wait();}
                    catch (InterruptedException e) {}
                    System.out.println(this.name + ": probuje znowu");
                }
            }
        }
        public synchronized void release() {
            System.out.println(this.name + " jest znowu gotowy");
            this.lock.unlock();
            notifyAll();
        }
    }
    public static void main(String[] args) throws InterruptedException {
        final Worker w1 = new Worker("w1");
        final Worker w2 = new Worker("w2");
        new Thread(() -> {w1.doWork(w2);}).start();
        new Thread(() -> {w2.doWork(w1);}).start();
    }
}
```
### Executor, callable
`Callable` w przeciwieństwie do `Runnable` mogą coś zwracać
```java
// chyba tu coś nie działa, bo chyba działa w nieskończość
import java.util.concurrent.*;
import java.util.*;

public class ParallelFor {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        ExecutorService es = Executors.newFixedThreadPool(16);
        Vector<Future> vf = new Vector<>();
        for(int i = 0; i < 10; i++) {
            final int no = i;
            Future<Object> f = es.submit(new Callable<Object>(){
                @Override
                public Object call() throws Exception {
                    return new Object();
                }
            });
            vf.add(f);
        }
        for(Future<Object> f : vf) {
            Object obj = f.get();
        }
    }
}
```
# Wykład 7
```java
import javax.swing.*;

public class HelloWorldSwing {
    private static void createAndShowGUI() {
        JFrame frame = new JFrame("HelloWorldSwing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JLabel label = new JLabel("Hello world");
        frame.getContentPane().add(label); // napis jest dodawany do zawartosci okna
        frame.pack(); // dopasowanie rozmiarow okna do umieszczonych w nim komponentow
        frame.setVisible(true);
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}
```
Kontenery najwyższego poziomu:
- JFrame
- JDialog (modalny)
- JApplet (w oknie przeglądarki)

JTextComponents:
- JTextField
- JFormattedTextField
- JPasswordField
- JTextArea
- JEditorPane
- JTextPane
### Własna przeglądarka
```java
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.URL;
import javax.swing.*;

public class Browser extends JFrame implements ActionListener {
    private static final String COMMAND_GO = "go";
    private JEditorPane webpage;
    private JTextField url;
    private JTextArea htmlPage;
    
    private JPanel createMainPanel() {
        JPanel mp = new JPanel();
        mp.setLayout(new BoxLayout(mp, BoxLayout.Y_AXIS));
        JPanel p = new JPanel();
        this.url = new JTextField();
        this.url.setPreferredSize(new Dimension(500, 20));
        this.url.setText( "http://www.simongrant.org/web/guide.html");
        JLabel l = new JLabel("adres");
        l.setLabelFor(this.url);
        p.add(l);
        p.add(this.url);
        JButton b = new JButton("Go");
        b.setActionCommand(COMMAND_GO);
        b.addActionListener(this);
        b.setPreferredSize(new Dimension(100, 40));
        p.add(b);
        mp.add(p);

        this.webpage = new JEditorPane();
        this.htmlPage = new JTextArea();
        try {
            this.setPage(new URL( "http://www.simongrant.org/web/guide.html"));
        } catch (IOException e) {}
        JTabbedPane tp = new JTabbedPane();
        tp.setPreferredSize(new Dimension(600, 400));
        JScrollPane sp = new JScrollPane(this.webpage);
        tp.add("page", sp);
        sp = new JScrollPane(this.htmlPage);
        tp.add("html", sp);
        mp.add(tp);
        return mp;
    }
    private void setPage(URL page) throws IOException {
        String s;
        this.webpage.setPage(page);
        BufferedReader br = new BufferedReader(new InputStreamReader(page.openStream()));
        while((s = br.readLine()) != null)
            this.htmlPage.append(s + "\n");
    }
    public Browser() {
        super();
        this.getContentPane().add(this.createMainPanel());
    }
    private static void createAndShow() {
        Browser b = new Browser();
        b.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        b.pack(); // dopasowanie rozmiarow okna do umieszczonych w nim komponentow
        b.setLocationRelativeTo(null); // żeby okienko się wyświetliło na środku, a nie w lewym górnym rogu
        b.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        if(COMMAND_GO.equals(e.getActionCommand())) {
            try {
                this.setPage(new URL(this.url.getText()));
            } catch (IOException e2) {
                this.webpage.setText("Problem z adresem " + this.url.getText());
                this.htmlPage.setText("Problem z adresem " + this.url.getText());
            }
        }
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShow();
            }
        });
    }
}
```
### JFileChooser, JOptionPane
może wybrać wiele plików
```java
import javax.swing.*;
import javax.swing.filechooser.*;

public class HelloWorldSwing {
    private static void JFC() {
        JFileChooser chooser = new JFileChooser();
        // chooser.setMultiSelectionEnabled(true);
        FileNameExtensionFilter filter = new FileNameExtensionFilter("Obrazy JPG i GIF", "jpg", "gif");
        chooser.setFileFilter(filter);
        int ret = chooser.showOpenDialog(null);
        if(ret == JFileChooser.APPROVE_OPTION) {
            System.out.println("Wybrales plik: " + chooser.getSelectedFile().getName());
        }
    }
    private static void JOPSMD() {
        JOptionPane.showMessageDialog(null, "Eggs are not supposed to be green.", "Inane warning", JOptionPane.WARNING_MESSAGE);
    }
    private static void JOPSID() {
        Object[] possibilities = {"ham", "spam", "yam"};
        String s = (String)JOptionPane.showInputDialog(null, "Complete the sentence:\n\"Green eggs and ...\"", "Customized dialog", JOptionPane.PLAIN_MESSAGE, null, possibilities,"ham");
        // possibilities can be null for text input
    }
    private static void createAndShowGUI() {
        JFrame frame = new JFrame("HelloWorldSwing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JLabel label = new JLabel("Hello world");
        frame.getContentPane().add(label); // napis jest dodawany do zawartosci okna
        frame.pack(); // dopasowanie rozmiarow okna do umieszczonych w nim komponentow
        JFC();
        JOPSMD();
        JOPSID();
        frame.setVisible(true);
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}
```
# Wykład 8
### URL
```java
import java.net.*;
import java.io.*;

public class URLExample {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://www.google.pl");
        BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
        String s;
        while((s = in.readLine()) != null)
            System.out.println(s);
        in.close();
    }
}
```
```java
import java.net.*;
import java.io.*;

public class URLConnectionExample {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://www.google.pl");
        URLConnection con = url.openConnection();
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String s;
        while((s = in.readLine()) != null)
            System.out.println(s);
        in.close();
    }
}
```
```java
import java.net.*;
import java.io.*;

public class URLConnectionWriter {
    public static void main(String[] args) throws Exception {
        URL url = new URL(args[0]);
        URLConnection con = url.openConnection();
        con.setDoOutput(true);
        OutputStreamWriter out = new OutputStreamWriter(con.getOutputStream());
        String s;
        for(int i = 1; i< args.length; i++)
            out.write(args[i]);
        out.close();
    }
}
```
Możemy rozmawiać przez:
- http
- https
- ftp, np: `ftp://login:haslo@serwer:port/katalog/podkatalog/plik`
- file
- jar
Inne przez implementację klasy `URLStreamHandler`. Zazwyczaj jednak zamiast tego używamy gniazd.
### Socket, klient
`Socket` do nawiązania jako klient połączenia z serwerem
Jest też `SSLSocket` oraz `SSLServerSocket` przez protokół SSL/TLS
W `TCP/IP` są zawsze pod spodem klient i serwer
```java
import java.net.Socket;
import java.io.*;

public class ClientExample {
    public static Socket sock;
    public static void main(String[] args) throws IOException {
        // Socket(adres, numer portu)
        sock = new Socket("127.0.0.1", Integer.valueOf("50000"));
        OutputStream os = sock.getOutputStream();
        InputStream is = sock.getInputStream();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String sLine;
        byte[] bRes = new byte[100];
        
        while((sLine = br.readLine()) != null) {
            os.write(sLine.getBytes());
            System.out.println("wyslalem: " + sLine);
            is.read(bRes); // wstrzymuje program czekając na odpowiedź serwera, instrukcja blokująca, lepiej to robić w osobnym wątku
            System.out.println("odebralem: " + new String(bRes));
        }
        br.close();
        sock.close();
    }
}
```
### Serwer echo
```java
import java.net.ServerSocket;
import java.net.Socket;
import java.io.*;

public class ServerExample {
    private static ServerSocket ss;
    public static void main(String[] args) throws IOException {
        ss = new ServerSocket(Integer.valueOf("50000"));
        while(true) {
            Socket s = ss.accept();
            InputStream is = s.getInputStream();
            OutputStream os = s.getOutputStream();
            int b;
            while((b = is.read()) != -1) {
                System.out.print((char)b);
                os.write(b);
            }
            s.close();
        }
    }
}
```
### SSL
```java
import javax.net.ssl.*;
import java.io.*;

public class EchoServer {
    public static void main(String[] args) throws IOException {
        SSLServerSocketFactory factory = (SSLServerSocketFactory) SSLServerSocketFactory.getDefault();
        SSLServerSocket ss = (SSLServerSocket) factory.createServerSocket(9999);
        SSLSocket s = (SSLSocket) ss.accept();
        BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
        String sTmp = null;
        while ((sTmp = br.readLine()) != null) {
            System.out.println(sTmp);
            System.out.flush();
        }
    }
}
```
```java
import javax.net.ssl.*;
import java.io.*;

public class EchoClient {
    public static void main(String[] args) throws IOException {
        SSLServerSocketFactory factory = (SSLServerSocketFactory) SSLServerSocketFactory.getDefault();
        SSLSocket s = (SSLSocket) factory.createServerSocket("localhost", 9999);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
        String sTmp = null;
        while ((sTmp = br.readLine()) != null) {
            bw.write(sTmp + '\n');
            bw.flush();
        }
    }
}
```
Żeby to zadziałało, to trzeba najpierw wygenerować klucze
`keytool -keygen -keystore mySrvKeystore -keyalg RSA`
Uruchomienie serwera
`java -Djavax.net.ssl.keyStore=mySrvKeystore -Djavax.net.ssl.keyStorePassword=123456 EchoServer`
Uruchomienie klienta
`java -Djavax.net.ssl.trustStore=mySrvKeystore -Djavax.net.ssl.trustStorePassword=123456 EchoClient`
Przykład: http://stilius.net/java/java_ssl.php

Da się wymusić autoryzację klienta
### Java Web Start
Lokalne uruchamianie programów w Java umieszczonych w sieci
- niezależna od przeglądarek
- możliwość wykorzystania wybranej wersji
- automatyczny update
- obsługuje prawa dostępu do zasobów lokalnego komputera (jeśli chcemy mieć `all-permissions`, to musimy podpisać wszystkie jar'y)
Opis zadania do uruchomienia wykorzystuje pliki jnlp (Java Network Launch Protocol) (pliki xml)
Trzeba jeszcze powiedzieć przeglądarce, że to jest plik jnlp (`mime`, `application/x-java-jnlp-file JNLP`)
# Wykład 9
### DOM - parser XML'a
Parser DOM (Document Object Model) - tworzy drzewo reprezentujące dane z dokumentu XML
```java
import java.io.*;
import java.net.URL;
import javax.xml.parsers.*;
import org.w3c.dom.*;
import org.xml.sax.SAXException;

public class DOMExample {
    static String content = """
<?xml version="1.0" encoding="UTF-8"?>
<catalog>
    <book id="bk101">
        <author>Gambardella, Matthew</author>
        <title>XML Developer's Guide</title>
        <genre>Computer</genre>
        <price>44.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>An in-depth look at creating applications with XML.</description>
    </book>
    <book id="bk102">
        <author>Ralls, Kim</author>
        <title>Midnight Rain</title>
        <genre>Fantasy</genre>
        <price>5.95</price>
        <publish_date>2000-12-16</publish_date>
        <description>A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.</description>
    </book>
</catalog>""";

    public static void main(String[] args) throws ParserConfigurationException, SAXException, IOException {
        URL url = new URL("http://www.w3schools.com/xml/plant_catalog.xml");
        DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
        // Document doc = dBuilder.parse(url.openStream());
        Document doc = dBuilder.parse(new ByteArrayInputStream(content.getBytes()));
        System.out.println("Root element: " + doc.getDocumentElement().getNodeName());
        NodeList nList = doc.getElementsByTagName("book");
        for(int i = 0; i < nList.getLength(); i++) {
            Node n = nList.item(i);
            if(n.getNodeType() == Node.ELEMENT_NODE) {
                Element e = (Element)n;
                System.out.println("Autor: " + getTagValue("author", e));
                System.out.println("Title: " + getTagValue("title", e));
            }
        }
    }
    private static String getTagValue(String s, Element e) {
        NodeList nl = e.getElementsByTagName(s).item(0).getChildNodes();
        Node n = (Node)nl.item(0);
        return n.getNodeValue();
    }
}
```
`node.setTextContent(), node.removeChild()`
### DOM - zapis
```java
Document doc = docBuilder.newDOcument();
Element e = doc.createElement("root");
doc.appendChild(e);

TransformerFactory transformerfactory = new TransformerFactory.newInstance();
Transformer transformer = transformerFactory.newTransformer();
DOMSource source = new DOMSource(doc);
StreamResult result = new StreamResult(new File("file.xml"));
transformer.transform(source, result);
```
### SAX - parser XML'a
Simple API for XML w miarę czytania dokumentu wywołuje zdarzenia związane z parsowaniem. Są szybsze i nie wymagają tyle pamięci, co DOM. Sami piszemy co ma się dziać jak występują te zdarzenia.
```java
import java.io.*;
import java.net.URL;
import javax.xml.parsers.*;
import org.w3c.dom.*;
import org.xml.sax.*;
import org.xml.sax.helpers.DefaultHandler;

public class SAXExample {
    static String content = """
<?xml version="1.0" encoding="UTF-8"?>
<catalog>
    <book id="bk101">
        <author>Gambardella, Matthew</author>
        <title>XML Developer's Guide</title>
        <genre>Computer</genre>
        <price>44.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>An in-depth look at creating applications with XML.</description>
    </book>
    <book id="bk102">
        <author>Ralls, Kim</author>
        <title>Midnight Rain</title>
        <genre>Fantasy</genre>
        <price>5.95</price>
        <publish_date>2000-12-16</publish_date>
        <description>A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.</description>
    </book>
</catalog>""";

    public static void main(String[] args) throws ParserConfigurationException, SAXException, IOException {
        SAXParserFactory f = SAXParserFactory.newInstance();
        SAXParser saxParser = f.newSAXParser();
        DefaultHandler handler = new ExampleSAXHandler();
        saxParser.parse(new ByteArrayInputStream(content.getBytes()), handler);
    }
    static class ExampleSAXHandler extends DefaultHandler {
        public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
            System.out.println("Element: " + qName);
        }
        public void endElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
            System.out.println("Koniec elementu: " + qName);
        }
        public void characters(char ch[], int start, int length) throws SAXException {
            System.out.println("zawartosc: " + new String(ch, start, length));
        }
    }
}
```
### JAXB
Java Architecture for XML Binding to standard serializacji XML dla obiektów Javy.
```java
import java.io.File;
import javax.xml.bind.*;
import javax.xml.bind.annotation.*;

// klasa do serializacji
@XmlRootElement
public class Person {
    String name;
    int age;
    public String getName() {return name;}
    @XmlElement
    public void setName(String name) {this.name = name;}
    public Integer getAge() {return age;}
    @XmlElement
    public void setAge(Integer age) {this.age = age;}
    public String toString() {
        return this.name + " (" + this.age + ") ";
    }
}
public class JAXBExample {
    public static void main(String[] args) throws JAXBException {
        Person p = new Person();
        p.setName("Barnaba");
        p.setAge(33);

        File f = new File("person.xml");
        JAXBContext ctx = JAXBContext.newInstance(Person.class);
        Marschaller marschaller = ctx.createMarschaller();
        marschaller.setProperty( Marschaller.JAXB_FORMATTED_OUTPUT, true);
        marschaller.marschal(p, System.out);
        marschaller.marschal(p, f);
        p = null;
        Unmarschaller unmarschaller = ctx.createUnmarschaller();
        p = (Person)unmarschaller.unmarschal(f);
        System.out.println(p);
    }
}
```
### XMLEncoder, XMLDecoder
```java
XMLEncoder e = new XMLEncoder(new FileOutputStream("jbutton.xml"));
e.writeObject(new JButton("Hello world"));
e.close();

XMLDecoder d = new XMLDecoder(new FileInputStream("jbutton.xml"));
obj = d.readObject();
d.close();
```
### Ant
Make w świecie Javy - automatyzacja procesów związanych z budowaniem programów.
Plik konfiguracyjny to `build.xml`
Aby wykonać ten plik piszemy w konsoli `ant`
Teraz częściej się używa Maven, Gradle, ale w nich pod spodem siedzi Ant
# Wykład 10
### SQL, JDBC
Structured Query Language
- `SELECT`
- `UPDATE`
- `DELETE`
- `INSERT`
np.:
```sql
SELECT Imie, Nazwisko FROM Tabela WHERE id = 3;
UPDATE Tabela SET Imie='Marek' WHERE id=4;
DELETE FROM Tabela WHERE Imie='Tomasz';
INSERT INTO Tabela (id, Imie) VALUES (5, 'DOROTA');
```
JDBC (Java Database Connectivity)  - specyfikacja określająca zbiór klas i interfejsów napisanych w Javie
Implementacja JDBC jest dostarczana przez producentów baz danych (zwykle biblioteka JAR)
```java
import java.sql.*;

public class TestDriver {
    public static void main(String[] args) {
        Statement stmt = null;
        ResultSet rs = null;
        try {
            Class.forName("org.hsqldb.jdbc.JDBCDriver").newInstance();
            Connection con = DriverManager.getConnection( "jdbc:hsqldb:mem:testdb", "sa", "");
            stmt = con.createStatement();
            rs = stmt.executeQuery("SELECT * FROM Tabela");
            // stmt.executeUpdate
            while(rs.next()) {
                System.out.println(rs.getString("Imie"));
            }
        } catch (Exception e) {
        } finally {
            if(rs != null) {
                try {rs.close();}
                catch (SQLException sqlEx) {}
                rs = null;
            }
            //tak samo stmt i con
        }
    }
}
```
### Metody nawiązywania połączenia z DB
`DriverManager` lub `DataSource` z usługą `JNDI` (Java Naming and Directory Interface). Z drugiego sposobu korzystamy w przypadku dużych, rozproszonych systemów.
```java
Context ctx = new InitialContext();
DataSource ds = (DataSource)ctx.lookup("jdbc/MojaDB");
Connection con = ds.getConnection("myLogin", "myPassword");
```
### Zapytania
tworzy się w ramach utworzonego wcześniej połączenia. Można wiele w ramach jednego statement.
- `Statement`
- `PreparedStatement` - prekompilowane zapytanie zawierające parametry wejściowe
- `CallableStatement` - zapisane w bazie danych
### HSQLDB
System zarządzania relacyjnymi bazami danych w całości napisany w Java (open source)
# Wykład 11
### getClass, forName
```java
import java.util.*;

enum Day {
            SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
}
public class Main {
    public static void main(String[] args) throws ClassNotFoundException {
        Class c;
        c = "foo".getClass();
        System.out.println(c.getName());
        c = System.out.getClass();
        System.out.println(c.getName());
        c = Day.SUNDAY.getClass();
        System.out.println(c.getName());
        byte[] bytes = new byte[1024];
        c = bytes.getClass();
        System.out.println(c.getName());
        Set<String> s = new HashSet<String>();
        c = s.getClass();
        System.out.println(c.getName());
        System.out.println("==========================");
        c = java.io.PrintStream.class;
        System.out.println(c.getName());
        c = int[][][].class;
        System.out.println(c.getName());
        c = boolean.class;
        System.out.println(c.getName());
        // c.getClass() to compile error
        //Class cMyClass = Class.forName("pl.edu.fais.java.Klasa");
        Class cDoubleArray = Class.forName("[D");
        // ClassNotFoundException jak nazwa klasy nie zostanie znaleziona
        System.out.println(cDoubleArray.getName());
        Class cStringArray = Class.forName("[[Ljava.lang.String;");
        System.out.println(cStringArray.getName());
    }
}
```
### Class methods
Wybrane metody klasy Class:
- `static Class<?> forName(String className)`
- `Constructor<T> getConstructor(Class<?>... parameterTypes)`
- `Constructor<?>[] getConstructors()`
- `Field getField(String name)`
- `Field[] getFields()`
- `Method getMethod(String name, Class<?>... parameterTypes)`
- `Method[] getMethods()`
```java


public class Main {
    public static void main(String[] args) {
        class C1 {}
        class C2 extends C1 {}
        C1 o1 = new C1(); // równoważne C1.class.newInstance()
        C2 o2 = new C2();
        System.out.println( o1.getClass().isAssignableFrom(o2.getClass()));
        System.out.println( o2.getClass().isAssignableFrom(o1.getClass()));
        System.out.println( o1.getClass().isInstance(o2));
        System.out.println( o2.getClass().isInstance(o1));
    }
}
```
```java
import java.lang.reflect.Field;

public class FieldExample {
    public static String s;
    public int i;
    public static void main(String[] args) throws Exception {
        FieldExample fex = new FieldExample();
        Field f;
        f = FieldExample.class.getField("s");
        f.get(null); // bo parametr statyczny
        f.set(null, "Ala"); // równoważne FieldExample.s = "Ala";
        f = fex.getClass().getField("i");
        f.set(fex, 10); // fex.i = 10;
    }
}
```
Metoda jest reprezentowana przez instancję klasy `Method`
```java
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class FieldExample {
    public static String s;
    public int i;
    public static void example3() {
        System.out.println("hi from example3");
    }
    public static void main(String[] args) throws Exception {
        FieldExample fex = new FieldExample();
        Field f;
        f = FieldExample.class.getField("s");
        f.get(null); // bo parametr statyczny
        f.set(null, "Ala"); // równoważne FieldExample.s = "Ala";
        f = fex.getClass().getField("i");
        f.set(fex, 10); // fex.i = 10;

        Method m = Class.forName("FieldExample").getDeclaredMethod("example3", null);
        m.invoke(null, null);
    }
}
```
### Dynamic proxy
Klasa `Proxy` udostępnia metody statyczne służące do tworzenia tzw. dynamicznych klas proxy oraz ich instancji. Utworzenie proxy dla np. MyInterface:
```java
public class Main {
    public static void main(String[] args) {
        InvocationHandler handler = new MyInvocationHandler(...);
        Class proxyClass = Proxy.getProxyClass( MyInterface.class.getClassLoader(), new Class[] {MyInterface.class});
        MyInterface mi = (MyInterface) proxyClass.getConstructor( new Class[] {InvocationHandler.class}).newInstance(new Object[] {handler});
    }
}
```
```java
public class Main {
    public static void main(String[] args) {
        InvocationHandler handler = new MyInvocationHandler(...);
        MyInterface mi = (MyInterface) Proxy.newProxyInstance( MyInterface.class.getClassLoader(), new Class[] {MyInterface.class}, handler);
    }
}
```
Korzystamy z refleksji, ale mamy kontrolę typów.
# Wykład 12
### Bytecode
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```
Na początku `.class` zawsze `CA FE BA BE`
### ASM
Biblioteka ułatwiająca manipulację bytecode'm Javy.
```java
import org.objectweb.asm.*;

public class MainDump implements Opcodes {
    public static byte[] dump() throws Exception {
        ClassWriter cw = new ClassWriter(0);
        MethodVisitor mv;
        cw.visit(V1_7, ACC_PUBLIC + ACC_SUPER, "Main", null, "java/langObject", null);
        mv = cw.visitMethod(ACC_PUBLIC, "<init>", "()V", null, null);
        mv.visitCode();
        ...
        return cw.toByteArray();
    }
}
public class HelloWorldASM extends CLassLoader {
    public static void main(final String args[]) throws Exception {
        HelloWorldASM loader = new HelloWorldASM();
        byte[] code = MainDump.dump();
        Class cl = loader.defineClass("Main", code, 0, code.length);
        cl.getMethods()[0].invoke(null, new Object[] {null});
    }
}
```
# Wykład 13
### Funkcje
```java
import java.util.function.*;

public class Main {
    public static void main(String[] args) {
        Runnable r = () -> {System.out.println("Hello");};
        Consumer<Integer> cons = x -> {System.out.println(x);};
        Supplier<Integer> sup = () -> 7;
    }
}
```
```java
import java.util.function.*;

public class Main {
    public static void main(String[] args) {
        // Function<typ argumentu, typ wartości zwracanej>
        Function<Integer, Integer> inc = x -> x+1;
        // BiFunction<typ argumentu1, typ argumentu1, typ wartości zwracanej>
        BiFunction<Integer, Integer, Integer> sum = (x, y) -> x+y;
        Function<Integer, Function<Integer, Integer>> sum1 = x->y->x+y;
        // funkcjonał - funkcja, która jako argument przyjmuje inną funkcją // metoda apply wylicza wartość funckji
        BiFunction<Function<Integer, Integer>, Integer, Integer> fx = (f, x) -> f.apply(x);
    }
}
```
W programowaniu funkcyjnym funkcje powinny działać zawsze tak samo i nie powinny powodować żadnych efektów ubocznych:
- wszystkie zmienne są final
- nie ma zmiennych globalnych
- funkcje mogą być argumentami i być zwracane
### `interface Function<T, R>`
- `R apply(T t)`
- `default <V> Function<T,V> andThen(Function<? super R,? extends V> after)`
- `default <V> Function<V,R> compose(Function<? super V,? extends T> before)`
### `interface Consumer<T>`
- `void accept(T t)`
- `default Consumer<T> andThen(Consumer<? super T> after)`
### `interface Supplier<T>`
- `T get()`
### `interface Predicate<T>`
- `boolean test(T t)`
- `default Predicate<T> and(Predicate<? super T> other)`
- `default Predicate<T> or(Predicate<? super T> other)`
- `default Predicate<T> negate()`
### `interface UnaryOperator<T>`
### Streams
```java
import java.util.stream.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Stream<String> objectStream = Stream.of("Ala", "Ola");
        String[] array = {"Ala", "Ola"};
        Stream<String> arrayStream = Arrays.stream(array);
        Stream.of(1, 2, 3).map(num -> num*num).forEach(System.out::println);
        Stream.of(1, 2, 3).map(num -> num*num).forEach(num -> System.out.println(num));
    }
}
```
```java
import java.util.stream.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> list1 = Arrays.asList(1, 2, 3);
        List<Integer> list2 = Arrays.asList(4, 5, 6);
        Stream.of(list1, list2).flatMap(List::stream).filter(num -> num%2 == 0).forEach(System.out::println);
    }
}
```
```java
import java.util.stream.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        String sentence = Stream.of("Hello", "world").collect(Collectors.joining(" "));
        System.out.println(sentence);
        Integer sum  = Stream.of(1, 2, 3).reduce(0, Integer::sum);
        System.out.println(sum);
    }
}
```