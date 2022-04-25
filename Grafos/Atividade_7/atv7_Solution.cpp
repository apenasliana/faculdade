#include <vector>
#include <cstdio>
#include <iostream>
using namespace std;

int numVertices, numArestas;
int cc[50001];
vector<int> listaAdj[50001];


void percorrer_dfs(int vertice){

    for(int index = 0;index < (int)listaAdj[vertice].size();index++){
        
        int aux = listaAdj[vertice][index];
        
        if(cc[aux] == -1){
            cc[aux] = cc[vertice];
            percorrer_dfs(aux);
        }
    }
}

int main(){
    

    cin >> numVertices >> numArestas;
    
    for(int index = 0; index < numVertices; index++) {
        cc[index] = -1; 
    }
    
    for(int index = 0; index < numArestas;index++){
        
        int partida, destino;
        cin >> partida >> destino ;

        listaAdj[partida-1].push_back(destino-1);
        listaAdj[destino-1].push_back(partida-1);
    }

    int id = 0;

    for(int index = 0;index < numVertices; index++){
        
        if(cc[index] == -1){ 
            id++;
            cc[index] = id;
            
            percorrer_dfs(index);
        }
        
    }
    cout << id;
    return 0;
}