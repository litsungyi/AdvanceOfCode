#include <iostream>
#include <fstream>
#include <climits>

int main(int argc, char** argv)
{
    int count = 0;
    int previous[4]{0};
    int current = 0;
    std::ifstream file("input.txt");
    int index = 0;
    while (file >> current)
    {
        previous[0] = previous[1];
        previous[1] = previous[2];
        previous[2] = previous[3];
        previous[3] = current;
        if (++index >= 4 && previous[0] < previous[3])
        {
            ++count;
        }
    }

    std::cout << count << std::endl;

    return 0;
}
