
#include <iostream>

using namespace std;


int main() {
    int nofarr, nofque,i;
    std::cin >> nofarr >> nofque;
    int **a = new int*[nofarr];
    for (i = 0; i < nofarr; i++) {
      /* code */
      int size;
      cin >> size;
      a[i] = new int[size];
      for(int j=0;j<size;j++){
        cin>> a[i][j];
      }
    }
    int result[nofque];
    for (i = 0; i < nofque; i++) {
      int row,column;
      cin>> row >> column;
      result[i] =  a[row][column];
    }
    for (i = 0; i < nofque; i++) {

        cout << result[i] << endl;
      }
    return 0;
}
