package Heranca;
import java.util.Date;
public class Escola {

	public static void main(String[] args) {
		Aluno aluno1 = new Aluno("Joao","09876546871",new Date());
		aluno1.matricula = "1";
		System.out.println("||Informacoes do aluno||");
		System.out.println("Nome:"+aluno1.nome);
		System.out.println("Cpf:"+aluno1.cpf);
		System.out.println("Matricula"+aluno1.matricula);
		
		
		Professor professor1 = new Professor("Gustavo","98765487653",new Date());
		professor1.salario= 2500;
		professor1.disciplina="Matematica";
		System.out.println("||Informacoes do professsor||");
		System.out.println("Nome professor:"+professor1.nome);
		System.out.println("Professor cpf:"+professor1.cpf);
		System.out.println("Salario:"+professor1.salario);
		System.out.println("Disciplina:"+professor1.disciplina);
	}

}
