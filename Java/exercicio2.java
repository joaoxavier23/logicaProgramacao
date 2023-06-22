import java.util.Scanner;
public class exercicio2 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Digite um numero");
		float resposta = scan.nextFloat();
		System.out.println("Digite um numero");
		float resposta2 = scan.nextFloat();
		System.out.println("Digite um numero");
		float resposta3 = scan.nextFloat();
		
		if (resposta>resposta2 && resposta>resposta3) {
			System.out.println("Maior: "+resposta);
		}
		else if (resposta2>resposta && resposta2>resposta3) {
			System.out.println("Maior:"+resposta2);
		}
		
		else {
			System.out.println("Maior:"+resposta3);
		}
		
		if (resposta<resposta2 && resposta<resposta3) {
			System.out.println("Menor:"+resposta);
		}
		else if (resposta2<resposta && resposta2<resposta3) {
			     System.out.println("Menor:"+resposta2);
		}
		else {
			 System.out.println("Menor:"+resposta3);
		}
		scan.close();
	}
	
}
