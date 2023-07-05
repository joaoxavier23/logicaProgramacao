import java.util.Scanner;

public class ExercicioArray4 {

	public static void main(String[] args) {
		int arrayA[] = new int[10];
		
		for (int i = 0; i!=10; i++) {
			Scanner scan = new Scanner(System.in);
			System.out.println("Digite o numero: ");
			arrayA[i]= scan.nextInt();
			
		}
		int arrayB[]= new int[10];
		for (int i = 0; i !=10; i++) {
			Scanner scan = new Scanner(System.in);
			System.out.println("Digite o numero: ");
			arrayB[i]= scan.nextInt();
		}
		int arrayC[]= new int[10];
		for (int i = 0; i !=10; i++) {
			Scanner scan = new Scanner(System.in);
			System.out.println("Digite o numero: ");
			arrayC[i]= scan.nextInt();
		}
		int arrayD[]= new int[10];
		for (int i = 0; i !=10; i++) {
			Scanner scan = new Scanner(System.in);
			System.out.println("Digite o numero: ");
			arrayD[i]= scan.nextInt();
		}
		for (int i:arrayA) {
			System.out.print(" "+i);
		}
		System.out.println("\n");
		for (int i:arrayB) {
			System.out.print(" "+i);
		}
		System.out.println("\n");
		for (int i:arrayC) {
			System.out.print(" "+i);
		}
		System.out.println("\n");
		for (int i:arrayD) {
			System.out.print(" "+i);
		}
	}

}
