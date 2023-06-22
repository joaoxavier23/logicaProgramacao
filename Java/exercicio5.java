import java.util.Scanner;
public class exercicio5 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Digite o seu sexo M ou F");
		char sexo = scan.next().charAt(0);
		
		if (sexo=='M'|| sexo=='m') {
			System.out.println("Masculino");
		}
		else if (sexo=='F' || sexo=='f') {
			System.out.println("Feminono");
		}
		else {
			System.out.println("Resposta invalida");
		}
	}

}
