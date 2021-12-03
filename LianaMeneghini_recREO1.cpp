#include <iostream>
#include <string>

using namespace std;

// não modifique os atuais atributos privados da classe!
class produto {
  friend class estoque;
  private:
    string descricao;
    unsigned preco;
  public:
  // aqui fica a seu critério
  produto();
  produto(string d, unsigned p);
};

produto::produto(string d, unsigned p){
    descricao = d;
    preco = p;
};

produto::produto(){
};

//##########################
// não modifique os atuais atributos privados da classe!
class estoque {
  private:
    unsigned numProdutos;
    produto* vetorDeProdutos;
  public:
  // aqui fica a seu critério
  estoque(unsigned n);
  ~estoque();
  void cadastraProduto(unsigned n, produto p);
  void redimensiona(unsigned n);
  void avaliaSaldo(unsigned s);
};

estoque::estoque(unsigned n){
    numProdutos = n;
    vetorDeProdutos = new produto[numProdutos];
};
estoque::~estoque(){
    delete [] vetorDeProdutos;
}

void estoque::cadastraProduto(unsigned n, produto p){
    vetorDeProdutos[n] = p;
};

void estoque::redimensiona(unsigned n){
    unsigned novacapacidade = n + numProdutos;
    
    //cria um vetor auxiliar para fazer a copia dos elementos
    produto* auxVet = vetorDeProdutos;
    vetorDeProdutos = new produto[novacapacidade];
    
    for (unsigned i = 0; i < numProdutos; i++)
    {
        vetorDeProdutos[i]= auxVet[i];
    }
    numProdutos = novacapacidade;
    delete [] auxVet;

};

void estoque::avaliaSaldo(unsigned s){

    // processo
    for(unsigned i = 0; i < numProdutos; i++) 
    {
      // facilitando a leitura das variaveis
      string nomeProduto = vetorDeProdutos[i].descricao;
      unsigned precoProduto = vetorDeProdutos[i].preco;

      // realizando a divisão
      unsigned quantidadeCompravel = s / precoProduto;

      // impressão do resultado
      cout << nomeProduto << " - " << quantidadeCompravel;
      if (quantidadeCompravel == 1)
      {
          cout << " unidade" <<endl;
      }else{
          cout << " unidades" <<endl;
      }
    }
    
}

// registro (estrutura) com dados de clientes
struct cliente { 
  string nome;
  unsigned saldo;
  cliente(string n, unsigned s);
};

cliente::cliente(string n, unsigned s){
    nome = n;
    saldo = s;
    

}


// não modifique a função principal sem autorização dos docentes
int main() {
  unsigned numProdutos;
  unsigned numNovosProdutos;
  string descricao;
  unsigned preco;

  unsigned numClientes;
  string nome;
  unsigned saldo;

  cin >> numProdutos;

  estoque meuEstoque(numProdutos);

  for (unsigned i = 0; i < numProdutos; i++) {
 
    cin >> descricao >> preco;
    produto umProduto(descricao,preco);
    meuEstoque.cadastraProduto(i,umProduto);
  }

  // aumenta o vetor de produtos com mais n novas posições
  
  cin >> numNovosProdutos;
  meuEstoque.redimensiona(numNovosProdutos);
  
  for (unsigned i = numProdutos; i < (numProdutos + numNovosProdutos); i++) {
    
    cin >> descricao >> preco;
    produto umProduto(descricao,preco);
    meuEstoque.cadastraProduto(i,umProduto);
  }

  
  cin >> numClientes;

  cliente** meusClientes = new cliente*[numClientes];

  for (unsigned i = 0; i < numClientes; i++) {
    
    cin >> nome >> saldo;
    meusClientes[i] = new cliente(nome,saldo);
  }

  // imprime relação de produtos que cada cliente consegue comprar
  for (unsigned i = 0; i < numClientes; i++) {
    cout << "###########################" << endl;
    cout << "Cliente - " << meusClientes[i]->nome << ":" << endl;
    meuEstoque.avaliaSaldo(meusClientes[i]->saldo);
    cout << endl;
  }

  return 0;
} 