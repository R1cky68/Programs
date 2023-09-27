/* This program has some shoulder conditions that have different attributes, then you answer some questions and it'll assign you one */
#include <stdio.h>
#include <iostream>

/* Class creation */
class shoulder {
    public:
    std::string name;
    bool onset;
    std::string pain;

};

int main() {

shoulder SLAP;
SLAP.name = "SLAP Lesion";
SLAP.onset = true;
SLAP.pain = "Deep";


shoulder LHB;
LHB.name = "LHB Tendinopathy";
LHB.onset = false;
LHB.pain = "Superficial";

shoulder ACJ;
ACJ.name = "ACJ Injury";
ACJ.onset = true;
ACJ.pain = "Superficial";

shoulder OA;
OA.name = "Osteoarthritis";
OA.onset = false;
OA.pain = "Deep";

std::cout << "Was the onset acute or chronic?" << std::endl;
std::string onset;
std::cin >> onset;

std::cout << "Is the pain superifical or deep?" << std::endl;

std::string pain;
std::cin >> pain;


if (onset == "Acute" && pain == "Deep") {
    std::cout << "You likely have a: " << SLAP.name << std::endl << SLAP.onset << std::endl << SLAP.pain << std::endl;
    return 0;

}

else if (onset == "Acute" && pain == "Superficial") {
    std::cout << "You likely have a: " << ACJ.name << std::endl << ACJ.onset << std::endl << ACJ.pain << std::endl;
    return 0;

}

else if (onset == "Chronic" && pain == "Superficial") {
    std::cout << "You likely have a: " << LHB.name << std::endl << LHB.onset << std::endl << LHB.pain << std::endl;
    return 0;

}

else if (onset == "Chronic" && pain == "Deep") {
    std::cout << "You likely have: " << OA.name << std::endl << OA.onset << std::endl << OA.pain << std::endl;
    return 0;

}

else {
    std::cout << "You've got something else then" << std::endl;
    return 0;
}

}