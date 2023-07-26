package Metodos;

public class Carro {
	private String cor;
	private double preco;
	private String modelo;
	
	public Carro(){
		
	}
	
	public Carro(String modelo, double preco) {
		this.cor= "preta";
		this.modelo= "modelo";
		this.preco= preco;
	}
	
	public Carro(String cor,String modelo,double preco) {
		this.cor= "cor";
		this.preco= preco;
		this.modelo= "modelo";
	}
	
}
