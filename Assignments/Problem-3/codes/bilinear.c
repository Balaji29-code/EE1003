// Function to perform bilinear transform on the differential equation
void bilinearTransform(double (*f)(double), double x0, double y0, double h, int n, double **results) {
    double x = x0; // Initialize x
    double y = y0; // Initialize y

    // Store initial values in the results array
    results[0][0] = x;
    results[0][1] = y;

    // Iterate over the number of steps
    for (int i = 1; i <= n; ++i) {
        double x_new = x + h; // Calculate new x value
        double y_new = y + h * f(x); // Calculate new y value (initial estimate)

        // Bilinear transform (Trapezoidal rule)
        y_new = y + (h / 2) * (f(x) + f(x_new));

        // Update x and y
        x = x_new;
        y = y_new;

        // Store updated values in the results array
        results[i][0] = x;
        results[i][1] = y;
    }
}

// Function representing the differential equation y' = 2x + 2
double differentialEquation(double x) {
    return 2 * x + 2;
}
