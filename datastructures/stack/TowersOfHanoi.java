import java.util.Scanner;


public class TowersOfHanoi {

  public void solve(int n, String start, String auxiliary, String end) {
    if (n == 1) {
      System.out.println(start + " -> " + end);
      System.out.println("Defaut size");
    } else {
      solve(n - 1, start, end, auxiliary);
      System.out.println(n - 1);
      System.out.println(start + " -> " + end);
      solve(n - 1, auxiliary, start, end);
   }
  }

  public static void main(String[] args) {
    TowersOfHanoi towersOfHanoi = new TowersOfHanoi();
    System.out.print("Enter number of discs: ");
    Scanner scanner = new Scanner(System.in);
    int discs = scanner.nextInt();
    towersOfHanoi.solve(discs, "A", "B", "C");
  }
}
