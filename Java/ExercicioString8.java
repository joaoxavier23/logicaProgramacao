
public class ExercicioString8 {

	public static void main(String[] args) {
		String valor = "CDD 4.0 - Java";
		
		System.out.println(valor.compareTo("CDD 4.0 - Java") == 0 ? true :false);
		System.out.println(valor.compareTo("CDD 4.0  Java") == 0 ? true :false);

	}

}
