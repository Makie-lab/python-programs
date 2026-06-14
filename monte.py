# Import the 'random' module — gives us functions to generate random numbers
import random

# Import matplotlib's pyplot — a library for drawing graphs and charts
import matplotlib.pyplot as plt


# Define a function called 'estimate_pi' that takes 'n' (number of points to throw, default 5000)
def estimate_pi(n=5000):

    # Create empty lists to store x and y coordinates of points that land INSIDE the circle
    inside_x, inside_y = [], []

    # Create empty lists to store x and y coordinates of points that land OUTSIDE the circle
    outside_x, outside_y = [], []

    # A counter to keep track of how many points landed inside the circle
    inside = 0

    # Empty list to store the running pi estimate after each point is thrown
    pi_estimates = []

    # Empty list to store the trial number (1, 2, 3, ...) for the convergence plot
    trials = []

    # Loop from 1 to n (we start at 1 so we can safely divide by i)
    for i in range(1, n + 1):

        # Generate a random x value between 0 and 1
        # Generate a random y value between 0 and 1
        x, y = random.random(), random.random()

        # Check if the point (x, y) falls inside the quarter-circle (distance from origin <= 1)
        if x**2 + y**2 <= 1:

            # If inside, increase the counter by 1
            inside += 1

            # Save this point's x coordinate to the "inside" list
            inside_x.append(x)

            # Save this point's y coordinate to the "inside" list
            inside_y.append(y)

        # If the point is NOT inside the quarter-circle
        else:

            # Save this point's x coordinate to the "outside" list
            outside_x.append(x)

            # Save this point's y coordinate to the "outside" list
            outside_y.append(y)

        # Calculate the current estimate of pi using all points thrown so far
        # Formula: pi ≈ 4 × (points inside circle) / (total points thrown)
        running_estimate = 4 * inside / i

        # Add this estimate to our list (for plotting later)
        pi_estimates.append(running_estimate)

        # Add the current trial number to our list
        trials.append(i)

    # After all points are thrown, calculate the final pi estimate
    pi_estimate = 4 * inside / n

    # Print the result to the screen, showing 5 decimal places
    print(f"Estimated π = {pi_estimate:.5f} (actual: 3.14159)")

    # --- SCATTER PLOT ---

    # Create a new figure (canvas) that is 6 inches by 6 inches
    plt.figure(figsize=(6, 6))

    # Plot all "inside" points as tiny blue dots
    plt.scatter(inside_x, inside_y, s=1, c="steelblue", label="Inside")

    # Plot all "outside" points as tiny red/coral dots
    plt.scatter(outside_x, outside_y, s=1, c="coral", label="Outside")

    # Set the title of the plot to show our pi estimate
    plt.title(f"Monte Carlo π ≈ {pi_estimate:.5f}")

    # Show a legend (the colored labels) with dots scaled up 5x so they're visible
    plt.legend(markerscale=5)

    # Display the scatter plot on screen
    plt.show()

    # --- CONVERGENCE PLOT ---

    # Create a new figure, wider (8 inches) and shorter (4 inches)
    plt.figure(figsize=(8, 4))

    # Draw a line showing how our pi estimate changed over time (purple line)
    plt.plot(trials, pi_estimates, c="purple", label="Running Estimate")

    # Draw a horizontal dashed black line at the actual value of pi for reference
    plt.axhline(y=3.14159, color="black", linestyle="--", label="Actual π")

    # Set the title of this plot
    plt.title("Convergence of Pi Estimate Over Time")

    # Label the x-axis
    plt.xlabel("Number of Trials")

    # Label the y-axis
    plt.ylabel("Estimated π")

    # Show the legend
    plt.legend()

    # Display the convergence plot on screen
    plt.show()


# Call the function with 10,000 random points
estimate_pi(10000)
