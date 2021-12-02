#include <iostream>
#include <fstream>
#include <climits>

int main()
{
    int count = 0;
    int previous = INT_MIN;
    int current = 0;
    std::ifstream file("input.txt");
    while (file >> current)
    {
        if (current > previous)
        {
            ++count;
        }

        previous = current;
    }

    std::cout << count << std::endl;

    return 0;
}

