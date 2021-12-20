#include <iostream>
#include <fstream>

class Point
{
public:
    Point()
        : x(0)
        , y(0)
        , aim(0)
    {}

    void Forward(int offset)
    {
        x += offset;
        y += aim * offset;
    }
    void Up(int offset) { aim -= offset; }
    void Down(int offset) { aim += offset; }
    
    int GetResult() const { return x * y; }

private:
    int x;
    int y;

    int aim;

};

int main(int argc, char** argv)
{
    Point position;
    std::ifstream file("input.txt");
    std::string direction;
    std::string value;
    while (file >> direction, file >> value)
    {
        auto v = std::stoi(value);
        if (direction == "forward")
        {
            position.Forward(v);
        }
        else if (direction == "up")
        {
            position.Up(v);
        }
        else if (direction == "down")
        {
            position.Down(v);
        }
    }

    std::cout << position.GetResult();

    return 0;
}
