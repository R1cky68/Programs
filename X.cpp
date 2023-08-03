/*This C++ program takes something as input then outputs different outputs, based on what you think x is you can play around with it */
#include <iostream> 
#include <string> 

int main() {
std::string Ans;
std::cout << "X can be anything. A symbol, an emotion, even more. What is X to you? \n";
std::cin >> Ans;

if (Ans == "Symbol")
    {
    std::cout << "X is a number now \n";
}

else if (Ans == "Emotion") 
{
    std::cout << "X is an emotion now, how do you feel about it is encapsulated \n";

} 

else if (Ans == "Char") {
        std::cout << "Nice! You've unlocked the hidden answer! Mega Man X is a chad! \n";
} 

else {
    std::cout << "We know it's tough. X has limitless possibilities so sometimes you can't put it into words \n";
}

return 0;
}
