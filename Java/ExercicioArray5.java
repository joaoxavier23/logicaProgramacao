import java.util.Scanner;
public class ExercicioArray5 {

	public static void main(String[] args) {
		double arrayNota[] = new double[5];
		double media=0;
		for (int i = 0; i < arrayNota.length; i++) {
			Scanner scan = new Scanner(System.in);
			System.out.println("Digite a nota do aluno: ");
			arrayNota[i] = scan.nextDouble();
			media+=arrayNota[i];
		}
		media=media/5;
		System.out.println("Media:"+media);
	}

}
