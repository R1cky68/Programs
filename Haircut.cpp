/* In this program you input a haircut and it prints each letter out with a space and capitalises it*/
#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>
#include <cctype>

std::string str() {
    char string[] = "j";
    return string;
} 

int main(){

std::cout << "Please enter a haircut and we'll edit it for you:" << std::endl;

std::string haircut;
std::cin >> haircut;

std::cout << "This is the haircut you entered: " << haircut << std::endl;


return 0;
}

/*
std::string str;
for (int i=0; i < std::__1::strlen(haircut); i++) {
    letter = std::toupper(haircut);
    std::cout << letter;

}*/