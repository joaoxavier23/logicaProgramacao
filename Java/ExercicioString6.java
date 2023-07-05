
public class ExercicioString6 {

	public static void main(String[] args) {
		String texto ="o rato roeu a roupa do rei de roma";
		int tamanho = texto.length();
		System.out.println(tamanho);
		String textoSemSpace = texto.trim().replaceAll("\\s+","");
		int tamanho2 = textoSemSpace.length();
		System.out.println(tamanho2);

	}

}
