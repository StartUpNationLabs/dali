#include <iostream>

#include "app.hpp"

App::App(std::string &&name) : name(std::move(name)) {}

void App::display(){
    std::cout << name << std::endl;
}