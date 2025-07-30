#include <iostream> // Include the input/output stream library for functions like std::cin and std::cout.

int main() { // The main function where program execution begins.
    int a, b;   // Declare two integer variables: 'a' and 'b' for input numbers.
    int sum;    // Declare an integer variable 'sum' for their total.

    // Read two integer inputs from the user, separated by a space, and store them in variables 'a' and 'b'.
    // std::cin automatically handles the space between the numbers.
    std::cin >> a >> b;

    // Calculate the sum of 'a' and 'b' and store it in the 'sum' variable.
    sum = a + b;

    // Print only the sum to the console, followed by a newline character.
    // std::endl also adds a newline and flushes the output buffer.
    std::cout << sum << std::endl;

    return 0; // Indicate successful program execution.
}