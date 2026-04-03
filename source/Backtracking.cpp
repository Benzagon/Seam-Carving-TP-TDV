#include "Backtracking.h"
#include <cmath>

std::vector<int> best = {}; // La costura vertical de menor energia (el camino rojo en columnas)

// PREGUNTAR SI ESTA OK
double best_energia = INFINITY; // Suma de energia en best_vec

void BT(const std::vector<std::vector<double>>& energia, int i, int j, int n, int m, std::vector<int>& curr, double curr_energia) {
    // CASO BASE
    if(i == n && j >= 0 && j < m){
        if(curr_energia < best_energia){
            best_energia = curr_energia;
            best = curr;
        }
    }
    // else if(best_energia < energia[i][j]){
    //     return;
    // }
    else if((j >= 0 && j < m) && best_energia >= curr_energia + energia[i][j]){
        curr.push_back(j);
        curr_energia += energia[i][j];
        
        // BAJO VERTICAL
        BT(energia, i+1, j, n, m, curr, curr_energia);
        // BAJO A LA IZQ
        BT(energia, i+1, j-1, n, m, curr, curr_energia);
        // BAJO A LA DER
        BT(energia, i+1, j+1, n, m, curr, curr_energia);
        
        curr.pop_back();
        curr_energia -= energia[i][j];
    }
}

std::vector<int> encontrarSeamBacktracking(const std::vector<std::vector<double>>& energia) {
    int n = energia.size();
    int m = energia[0].size();
    
    std::vector<int> curr = {};
    double curr_energia = 0;

    for(int i = 0; i < m; i++){
        BT(energia, 0, i, n, m, curr, curr_energia);
    }
    return best;
}
