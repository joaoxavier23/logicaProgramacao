import java.util.Scanner;
public class Exercicio1 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		 System.out.println("Digite um número: ");
		 float resposta = scan.nextFloat();
		 System.out.println((resposta>0 ? "positivo" : "negativo"));
		 scan.close();

	}

}
