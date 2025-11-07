# Trigonometric Functions Calculator
import math

def trigonometric_calculator():
    print("Welcome, Harina! Let's explore Trigonometric Functions!")
    print("---------------------------------------------------------")

    # Take angle input from user
    angle_deg = float(input("Enter the angle in degrees: "))

    # Convert degrees to radians
    angle_rad = math.radians(angle_deg)

    # Calculate trigonometric values
    sine = math.sin(angle_rad)
    cosine = math.cos(angle_rad)
    tangent = math.tan(angle_rad)

    # Print results
    print(f"\nTrigonometric values for {angle_deg}° are:")
    print(f"Sine (sin θ)   = {sine:.4f}")
    print(f"Cosine (cos θ) = {cosine:.4f}")

    # Handle undefined tangent values
    if math.isclose(cosine, 0, abs_tol=1e-9):
        print("Tangent (tan θ) = Undefined (cos θ = 0)")
    else:
        print(f"Tangent (tan θ) = {tangent:.4f}")

# Run the program
if __name__ == "__main__":
    trigonometric_calculator()
