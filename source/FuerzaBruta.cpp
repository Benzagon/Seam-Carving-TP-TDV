#include "FuerzaBruta.h"
#include <cmath>

// O(3^n)
void FB(const std::vector<std::vector<double>>& energia, int i, int j, int n, int m, std::vector<int>& curr, double curr_energia, std::vector<int>& best, double* best_energia) {
    // CASO BASE
    if(i == n && j >= 0 && j < m){
        if(curr_energia < *best_energia){
            *best_energia = curr_energia;
            best = curr;
        }
    }
    else if(j >= 0 && j < m){
        curr.push_back(j);
        curr_energia += energia[i][j];
        
        // BAJO VERTICAL
        FB(energia, i+1, j, n, m, curr, curr_energia, best, best_energia);
        // BAJO A LA IZQ
        FB(energia, i+1, j-1, n, m, curr, curr_energia, best, best_energia);
        // BAJO A LA DER
        FB(energia, i+1, j+1, n, m, curr, curr_energia, best, best_energia);
        
        curr.pop_back();
        curr_energia -= energia[i][j];
    }
}

// O(3^n * m)
// tita(n)
std::vector<int> encontrarSeamFuerzaBruta(const std::vector<std::vector<double>>& energia) {
    int n = energia.size();
    int m = energia[0].size();
    
    std::vector<int> curr = {};
    double curr_energia = 0;

    std::vector<int> best = {}; // La costura vertical de menor energia (el camino rojo en columnas)
    double best_energia = INFINITY; // Suma de energia en best_vec

    //O(m * 3^n)
    for(int i = 0; i < m; i++){
        FB(energia, 0, i, n, m, curr, curr_energia, best, &best_energia);
    }
    return best;
}