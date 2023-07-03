import java.util.Scanner;

public class ExercicioWhile2 {

	public static void main(String[] args) {
		int alunosConta=0;
		float alunosNota=0;
		float alunosNota2=0;
		Scanner scan = new Scanner(System.in);
		System.out.println("Digite quantos alunos tem na sala: ");
		int alunos = scan.nextInt();
		
		while (alunosConta!=alunos) {
			Scanner scan2 = new Scanner(System.in);
			System.out.println("Digite a nota do aluno: ");
			alunosNota= scan2.nextFloat();
			alunosConta++;
			alunosNota2= alunosNota2+alunosNota;
		
		}
	
		float media=alunosNota2/alunos;
		System.out.println(media);
	}
	
}
