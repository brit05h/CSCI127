//name:Britney Huiracocha
//email:britney.huiracocha44@myhunter.cuny.edu
//date:November 29, 2020
//this program writes a C++ program that asks the user

#include <iostream>
using namespace std;

int main ()
{
    int n;
    cout<< "Enter a number:";
    cin >> n;
    int x;
    
    if (n <0 )
    {
        cout<< "1";
        x = 32 +n;
    }
    else
    {
        cout << "0";
        x = n;
    }
    int b = 16;
    while (b > 0.5)
    {
        if (x >= b)
        {
            cout << "1";
        }
        else
        {
            cout << "0";
        }
        
        x = x % b ;
        b = b/2;
    }
    cout << "\n";
    return 0;
}
