package Math;

public class Calculadora {
	public static void main(String[] args) {
		Operacoes op1 = new Operacoes();
		
		Operacoes op2 = new Operacoes(1,2);
		System.out.println("Operacoes 2: "+op2.um+" "+op2.dois);
		
		Operacoes op3 = new Operacoes(3,4,5);
		System.out.println("Operacoes 3: "+op3.um+" "+op3.dois+" "+op3.tres);
		
		op2.somar(4,4);
		op3.somar(9,9,2);
		op2.dividir(8, 2);
		op2.multiplicar(5, 5);
		op2.subtrair(2,2);
	}
}
