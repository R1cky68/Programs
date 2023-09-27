/* This program monitors computer parameters like disk space, CPU , memory or disk usage and tells you when it's been exceeded */
#include <iostream>
#include <stdio.h>
#include <sys/types.h>
#include <sys/sysctl.h>
#include <sys/param.h>
#include <sys/mount.h>

#define BUFFERLEN 128

int main() 
{

int refresh = 5;
int Memory[2] = {8, 16};

/* This calls CPU info */
char buffer[BUFFERLEN];
size_t bufferlen = BUFFERLEN;
sysctlbyname ("machdep.cpu.brand_string", &buffer, &bufferlen, NULL, 0);

/* This provides details about the disk space and helps convert it to GB */
struct statfs statf;
statfs(".", &statf);
int GB = 1e9;

/* This is the memory display, outputting the RAM (random access memory) in bytes, ie 859934592 */
int mib [] = {CTL_HW, HW_MEMSIZE};
int64_t value = 0;
size_t length = sizeof(value);

if(-1 == sysctl(mib, 2, &value, &length, NULL, 0)) {
    std::cout << "Error" << std::endl;

}

/* Here they choose what they want to monitor */
do {
    std::cout << "Welcome, what would you like to monitor? \nCPU usage \nDisk Space \nMemory usage \nExit" << std::endl;
    std::string choice;
    std::cin >> choice;

    if (choice == "CPU") {
        std::cout << buffer << std::endl;
        
    }

    /* Total disk space given by multiplying the amount of bytes in each block (statf.f_bsize) with the total number of block (stat.f_blocks) */
    else if (choice == "Disk") {
        std::cout << "Total storage = " << (statf.f_blocks * statf.f_bsize) / GB << " GB" << std::endl;
        std::cout << "Used storage = " << ((statf.f_blocks * statf.f_bsize) - (statf.f_bavail * statf.f_bsize)) / GB << " GB" << std::endl;
        std::cout << "Available space (admin) = " << (statf.f_bavail * statf.f_bsize) / GB << " GB" << std::endl;
        std::cout << "Available space (guest) = " << (statf.f_bfree * statf.f_bsize) / GB << " GB" << std::endl;
        
    }

    /* For memory just converting to GB */
    else if (choice == "Memory") {
        std::cout << "Memory = " << value / GB << " GB" << std::endl;
        
    }

    else if (choice == "Exit") {
        std::cout << "Exited" << std::endl;
        break;
    }

    else {
        std::cout << "Still working on this part" << std::endl;

    }

} while (true);

return 0;
}