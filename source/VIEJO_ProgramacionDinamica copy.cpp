// #include "ProgramacionDinamica.h"
// #include <cmath>
// #include <limits>

// std::pair<std::vector<int>, double> min_carving(std::pair<std::vector<int>, double> abajo, std::pair<std::vector<int>, double> izq, std::pair<std::vector<int>, double> der) {
//     if(izq.second <= abajo.second && izq.second <= der.second){
//         return izq;
//     }
//     else if(der.second <= abajo.second && der.second <= izq.second){
//         return der;
//     }
//     return abajo;
// }

// std::pair<std::vector<int>, double> PD(const std::vector<std::vector<double>>& energia, int i, int j, int n, int m, std::vector<std::vector<std::pair<std::vector<int>, double>>> & memo) {
//     if(j >= 0 && j < m) {
//         // Si ya calcule la pos
//         if(!std::isnan(memo[i][j].second)){
//             return memo[i][j];
//         }
//         // CASO BASE
//         else if(i == n-1){
//             std::pair<std::vector<int>, double> elem = {{j}, energia[i][j]};
//             memo[i][j] = elem;
//             return elem;
//         }
//         else {
//             // BAJO VERTICAL
//             std::pair<std::vector<int>, double> abajo = PD(energia, i+1, j, n, m, memo);
//             // BAJO A LA IZQ
//             std::pair<std::vector<int>, double> izq = PD(energia, i+1, j-1, n, m, memo);
//             // BAJO A LA DER
//             std::pair<std::vector<int>, double> der = PD(energia, i+1, j+1, n, m, memo);
            
//             std::pair<std::vector<int>, double> min = min_carving(abajo,izq,der);

//             min.first.insert(min.first.begin(), j);
//             min.second += energia[i][j];

//             memo[i][j] = min;
//             return min;
//         }
//     }

//     std::pair<std::vector<int>, double> INVALIDO = {{}, INFINITY};
//     return INVALIDO;
// }

// // O(n*m)
// // tita((n^2)*m)
// std::vector<int> encontrarSeamPD(const std::vector<std::vector<double>>& energia) {
//     int n = energia.size();
//     int m = energia[0].size();

//     std::vector<std::vector<std::pair<std::vector<int>, double>>> memo = {};

//     // Popular memo de elementos vacios.
//     for (int i = 0; i < n; i++){
//         std::vector<std::pair<std::vector<int>, double>> fila = {};
//         for(int j = 0; j < m; j++){
//             std::pair<std::vector<int>, double> elem = {{}, std::numeric_limits<double>::quiet_NaN()};
//             fila.push_back(elem);
//         }
//         memo.push_back(fila);
//     }

//     std::vector<int> best = {};
//     double best_energia = INFINITY; 

//     for(int i = 0; i < m; i++){
//         std::pair<std::vector<int>, double> stream = PD(energia, 0, i, n, m, memo);
//         if(stream.second < best_energia){
//             best = stream.first;
//             best_energia = stream.second;
//         }
//     }
//     return best;
// }