import java.util.Scanner;

public class ExercicioWhile4 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		System.out.println("Digite um numero: ");
		int numero = scan.nextInt();
		int contadorPar=0;
		int contadorImpar=0;
		while (contadorPar!=numero) {
			if (contadorPar%2==0) {
				System.out.print("Numeros pares:"+contadorPar+" " );
			}
			
			contadorPar++;
		}
		while (contadorImpar!=numero) {
			if (contadorImpar%2!=0) {
				System.out.print("Numeros impares:"+contadorImpar+" ");
			}
			contadorImpar++;
		}
	

	}

}
