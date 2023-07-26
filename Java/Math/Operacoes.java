package Math;

public class Operacoes {

	int um;
	int dois;
	int tres;
	
	public Operacoes() {
		
	}
	
	public Operacoes(int um, int dois) {
		this.um=um;
		this.dois=dois;

	}
	public Operacoes(int um, int dois,int tres) {
		this.um=um;
		this.dois=dois;
		this.tres=tres;
	}
	public void somar(int um,int dois) {
		System.out.println(um+dois);
	}
	public void somar(int um,int dois,int tres) {
		System.out.println(um+dois+tres);
	}
	public void subtrair(int um,int dois) {
		System.out.println(um-dois);
	}
	public void subtrair(int um,int dois,int tres) {
		System.out.println(um-dois-tres);
	}
	public void multiplicar(int um,int dois) {
		System.out.println(um*dois);
	}
	public void multiplicar(int um,int dois,int tres) {
		System.out.println(um*dois*tres);
	}
	public void dividir(int um,int dois) {
		System.out.println(um/dois);
	}
	public void dividir(int um,int dois,int tres) {
		System.out.println(um/dois/tres);
	}
}
