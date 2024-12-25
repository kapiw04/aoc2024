#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>

bool comp(int a, int b)
{
    return a < b;
}

int main(int argc, char const *argv[])
{
    std::ifstream input("input");
    std::string line;

    std::vector<int> list1;
    std::vector<int> list2;

    while (getline(input, line))
    {
        std::stringstream ss(line);
        std::string num;
        std::vector<std::string> temp;
        while (getline(ss, num, ' '))
        {
            temp.push_back(num);
        }
        list1.push_back(std::stoi(temp[0]));
        list2.push_back(std::stoi(temp[1]));
    }

    long long int distance = 0;
    std::sort(list1.begin(), list1.end(), comp);
    std::sort(list2.begin(), list2.end(), comp);
    list1.erase(unique(list1.begin(), list1.end()), list1.end());

    for (int i = 0; i < list1.size(); i++)
    {
        distance += std::count(list2.begin(), list2.end(), list1[i]) * list1[i];
    }

    std::cout << distance << std::endl;

    return 0;
}
