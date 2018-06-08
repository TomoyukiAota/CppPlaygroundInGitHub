#include "Hello.h"
#include <iostream>

int main()
{
    const auto helloWorld = getHelloWorld();
    std::cout << helloWorld << std::endl;
    std::cin.get();
}