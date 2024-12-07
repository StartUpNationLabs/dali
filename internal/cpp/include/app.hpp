#ifndef APP_HPP
#define APP_HPP

#include <string>

class App {
private:
    std::string name;    

public:
    App(std::string &&name);
    void display();
    
   
};

#endif
