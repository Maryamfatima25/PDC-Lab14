
import sys
import datetime

def main():
    print("=" * 45)
    print("       PDC LAB 14 - JENKINS BUILD")
    print("=" * 45)

    print("\n1. Python environment")
    print("Python version:", sys.version)

    print("\n2. Running calculations")

    a = 10
    b = 20

    print("First number:", a)
    print("Second number:", b)
    print("Addition:", a + b)
    print("Subtraction:", b - a)
    print("Multiplication:", a * b)

    print("\n3. Running tests")

    assert a + b == 30
    assert b - a == 10
    assert a * b == 200

    print("All tests passed successfully!")

    print("\n4. Build information")
    print("Build date:", datetime.datetime.now())
    print("Jenkins Python execution successful!")

    print("=" * 45)


if __name__ == "__main__":
    main()

