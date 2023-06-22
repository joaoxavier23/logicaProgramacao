import java.util.Scanner;
public class exercicio6 {
	public static void main(String[] args) {
		int contador = 0;
		Scanner scan = new Scanner(System.in);
		System.out.println("Telefonou para a vitima?");
		char resposta1= scan.next().charAt(0);
		System.out.println("Esteve no local do crime?");
		char resposta2= scan.next().charAt(0);
		System.out.println("Mora perto da vitima?");
		char resposta3= scan.next().charAt(0);
		System.out.println("Devia para a vitima?");
		char resposta4=scan.next().charAt(0);
		System.out.println("Ja trabalhou para a vitima?");
		char resposta5=scan.next().charAt(0);
		
		if (resposta1=='S' || resposta1=='s') {
			contador++;
		}
		if (resposta2=='S' || resposta2=='s') {
			contador++;
		}
		if (resposta3=='S' || resposta3=='s') {
			contador++;
		}
		if (resposta4=='S' || resposta4=='s') {
			contador++;
		}
		if (resposta5=='S' || resposta5=='s') {
			contador++;
		}
		if (contador==2) {
			System.out.println("Suspeito");
		}
		if (contador==3 || contador==4) {
			System.out.println("Cumplice");
		}
		if (contador==5) {
			System.out.println("Assassino");
		}
		if (contador==0 || contador==1) {
			System.out.println("Inocente");
		}
		scan.close();
	}
	
}
