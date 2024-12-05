#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>

bool is_safe(const std::vector<int> &levels)
{
    for (int i = 1; i < levels.size(); ++i)
    {
        int diff = abs(levels[i] - levels[i - 1]);
        if (diff < 1 || diff > 3)
            return false;
    }
    return std::is_sorted(levels.begin(), levels.end(), std::less<int>()) || std::is_sorted(levels.begin(), levels.end(), std::greater<int>());
}

int main()
{
    std::ifstream input("input");
    std::string line;
    int count = 0;

    while (std::getline(input, line))
    {
        std::stringstream ss(line);
        std::vector<int> levels;
        int num;
        while (ss >> num)
        {
            levels.push_back(num);
        }

        if (is_safe(levels))
        {
            ++count;
            continue;
        }

        bool became_safe = false;
        for (size_t i = 0; i < levels.size(); ++i)
        {
            std::vector<int> modified = levels;
            modified.erase(modified.begin() + i);
            if (is_safe(modified))
            {
                became_safe = true;
                break;
            }
        }

        if (became_safe)
            ++count;
    }

    std::cout << count << std::endl;

    return 0;
}
