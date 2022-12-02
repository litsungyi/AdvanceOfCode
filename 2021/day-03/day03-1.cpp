#include <iostream>
#include <fstream>
#include <vector>

int main(int argc, char** argv)
{
    std::ifstream file("input.txt");
    std::vector<int> counts {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    std::string line;
    auto total = 0;
    while (file >> line)
    {
        ++total;
        for (auto i = 0; i < line.length(); ++i)
        {
            auto ch = line[i];
            if (ch == '1') {
                ++counts[i];
            }
        }
    }

    auto gamma = 0;
    auto epsilon = 0;
    total >>= 1;
    for (auto count : counts)
    {
        gamma <<= 1;
        epsilon <<= 1;
        if (count >= total)
        {
            gamma += 1;
        }
        else
        {
            epsilon += 1;
        }
    }

    std::cout << gamma * epsilon;

    return 0;
}
