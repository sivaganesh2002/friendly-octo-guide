#include <iostream>
#include <vector>
#include <string>

int main() {
    // Check for correct number of command-line arguments.
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <n>" << std::endl;
        return 1;
    }

    int n;
    try {
        n = std::stoi(argv[1]);
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << argv[1] << " is not a valid integer." << std::endl;
        return 1;
    } catch (const std::out_of_range& e) {
        std::cerr << "Input number is out of range." << std::endl;
        return 1;
    }

    // Constraints check
    if (n < 1 || n > 1000) {
        std::cerr << "Constraint violation: n must be between 1 and 1000." << std::endl;
        return 1;
    }

    std::vector<std::string> result;

    for (int i = 1; i <= n; ++i) {
        if (i % 3 == 0 && i % 5 == 0) {
            result.push_back("FizzBuzz");
        } else if (i % 3 == 0) {
            result.push_back("Fizz");
        } else if (i % 5 == 0) {
            result.push_back("Buzz");
        } else {
            result.push_back(std::to_string(i));
        }
    }

    // Print the output vector
    for (size_t i = 0; i < result.size(); ++i) {
        std::cout << result[i];
    }

    return 0;
}