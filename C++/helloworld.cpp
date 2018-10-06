#include <iostream>
#include <vector>
#include <string>

std::vector<char> Alphabet {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
std::vector<int> HelloWorldCode {7, 4, 11, 11, 14, 22, 14, 17, 11, 3};

int main()
{
    std::string message;
    for(auto index : HelloWorldCode){
        message += Alphabet.at(index);
    }
    std::cout << message << '\n';
}
