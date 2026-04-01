#include "FuerzaBruta.h"
#include <cmath>

std::vector<int> best = {}; // La costura vertical de menor energia (el camino rojo en columnas)

// PREGUNTAR SI ESTA OK
double best_energia = INFINITY; // Suma de energia en best_vec

void FB(const std::vector<std::vector<double>>& energia, int i, int j, int n, int m, std::vector<int>& curr, int curr_energia) {
    // CASO BASE
    if(i == n && j >= 0 && j < m){
        if(curr_energia < best_energia){
            best_energia = curr_energia;
            best = curr;
        }
    }
    else if(j >= 0 && j < m){
        curr.push_back(j);
        curr_energia += energia[i][j];
        
        // BAJO VERTICAL
        FB(energia, i+1, j, n, m, curr, curr_energia);
        // BAJO A LA IZQ
        FB(energia, i+1, j-1, n, m, curr, curr_energia);
        // BAJO A LA DER
        FB(energia, i+1, j+1, n, m, curr, curr_energia);
        
        curr.pop_back();
        curr_energia -= energia[i][j];
    }
}

std::vector<int> encontrarSeamFuerzaBruta(const std::vector<std::vector<double>>& energia) {
    std::vector<int> curr = {};
    double curr_energia = 0;
    FB(energia, 0, 0, energia.size(), energia[0].size(), curr, curr_energia);
    return best;
}
