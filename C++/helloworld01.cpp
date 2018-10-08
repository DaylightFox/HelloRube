#include <iostream>
#include <string>

void addHToString(std::string &str){
    str += 'H';
}

void addEToString(std::string &str){
    str += 'E';
}

void addLToString(std::string &str){
    str += 'L';
}

void addOToString(std::string &str){
    str += 'O';
}

void add_ToString(std::string &str){
    str += '_';
}

void addWToString(std::string &str){
    str += 'W';
}

void addRToString(std::string &str){
    str += 'R';
}

void addDToString(std::string &str){
    str += 'D';
}

void addExclamationMarkToString(std::string &str){
    str += '!';
}

int main(){
    std::string message;
    addHToString(message);
    addEToString(message);
    addLToString(message);
    addLToString(message);
    addOToString(message);
    add_ToString(message);
    addWToString(message);
    addOToString(message);
    addRToString(message);
    addLToString(message);
    addDToString(message);
    addExclamationMarkToString(message);
    std::cout << message << '\n';
}
