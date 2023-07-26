package Math;

public class Fazenda {

	public static void main(String[] args) {
		cachorro cachorro1 = new cachorro("bill",1);
		cachorro1.emitirSom="auau";
		System.out.println(cachorro1.nome);
		System.out.println(cachorro1.emitirSom);
		cachorro1.locomover();
		
		Gato gato1 = new Gato("billy",2);
		gato1.emitirsom="miau";
		System.out.println(gato1.nome);
		System.out.println(gato1.emitirsom);
		
		Ave ave1 = new Ave("chico",1);
		System.out.println(ave1.nome);
		ave1.cantar="cantando";
		ave1.voar();

	}

}
