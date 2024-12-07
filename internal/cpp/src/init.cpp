#include <iostream>

#include "init.hpp"

Init::Init(){
    std::cout << "void setup() {\n";
};

void Init::device(const int &pinNumber){
    std::cout << "pinMode(" << pinNumber << ", OUTPUT); \n";
}
void Init::sensor(const int &pinNumber){
    std::cout << "pinMode(" << pinNumber << ", INPUT); \n";

}
void Init::endInit(){
    std::cout << "\n}\n";
    std::cout << "\nvoid loop() {\nstep0();\n}\n\n";
}

