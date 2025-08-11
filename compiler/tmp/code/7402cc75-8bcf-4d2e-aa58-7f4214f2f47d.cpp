#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<string> result;

    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0)
            result.push_back("FizzBuzz");
        else if (i % 3 == 0)
            result.push_back("Fizz");
        else if (i % 5 == 0)
            result.push_back("Buzz");
        else
            result.push_back(to_string(i));
    }

    // Print the result
    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i != result.size() - 1) cout << " ";
    }

    return 0;
}