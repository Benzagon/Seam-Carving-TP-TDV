// #include "ProgramacionDinamica.h"
// #include <cmath>
// #include <limits>

// std::pair<int, double> min_carving(std::pair<int, double> abajo, std::pair<int, double> izq, std::pair<int, double> der, int j) {
//     if(izq.second <= abajo.second && izq.second <= der.second){
//         return {j-1, izq.second};
//     }
//     else if(der.second <= abajo.second && der.second <= izq.second){
//         return {j+1, der.second};
//     }
//     return {j, abajo.second};
// }

// std::pair<int, double> PD(const std::vector<std::vector<double>>& energia, int i, int j, int n, int m, std::vector<std::vector<std::pair<int, double>>> & memo) {
//     if(j >= 0 && j < m) {
//         // Si ya calcule la pos
//         if(!std::isnan(memo[i][j].second)){
//             return memo[i][j];
//         }
//         // CASO BASE
//         else if(i == n-1){
//             std::pair<int, double> elem = {-1, energia[i][j]};
//             memo[i][j] = elem;
//             return elem;
//         }
//         else {
//             // BAJO VERTICAL
//             std::pair<int, double> abajo = PD(energia, i+1, j, n, m, memo);
//             // BAJO A LA IZQ
//             std::pair<int, double> izq = PD(energia, i+1, j-1, n, m, memo);
//             // BAJO A LA DER
//             std::pair<int, double> der = PD(energia, i+1, j+1, n, m, memo);
            
//             std::pair<int, double> min = min_carving(abajo,izq,der,j);

//             min.second += energia[i][j];

//             memo[i][j] = min;
//             return min;
//         }
//     }

//     std::pair<int, double> INVALIDO = {{}, INFINITY};
//     return INVALIDO;
// }

// // Funcion para reconstruir la solucion en el memo
// std::vector<int> reconstruir(std::vector<std::vector<std::pair<int, double>>> & memo, int best, int n){
//     std::vector<int> res = {};
//     res.push_back(best);
//     int prev = best;
//     for(int i = 0; i < n-1; i++){
//         res.push_back(memo[i][prev].first);
//         prev = memo[i][prev].first;
//     }
//     return res;
// }

// // O(n*m)
// // tita(n*m)
// std::vector<int> encontrarSeamPD(const std::vector<std::vector<double>>& energia) {
//     int n = energia.size();
//     int m = energia[0].size();

//     std::vector<std::vector<std::pair<int, double>>> memo = {};

//     // Popular memo de elementos vacios.
//     for (int i = 0; i < n; i++){
//         std::vector<std::pair<int, double>> fila = {};
//         for(int j = 0; j < m; j++){
//             std::pair<int, double> elem = {-1, std::numeric_limits<double>::quiet_NaN()};
//             fila.push_back(elem);
//         }
//         memo.push_back(fila);
//     }

//     int best = -1;
//     double best_energia = INFINITY; 

//     for(int i = 0; i < m; i++){
//         std::pair<int, double> stream = PD(energia, 0, i, n, m, memo);
//         if(stream.second < best_energia){
//             best = stream.first;
//             best_energia = stream.second;
//         }
//     }

//     return reconstruir(memo, best, n);
// }