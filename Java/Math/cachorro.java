package Math;

public class cachorro extends Animal{
	
	public  cachorro(String _nome, int _idade) {
		super(_nome,_idade);
	}
	public String emitirSom;
	public void locomover() {
		System.out.println("o cachorrro andou");
	}
}
