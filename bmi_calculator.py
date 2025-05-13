from typing import Optional
def calculate_bmi(weight: float, height: float) -> Optional[float]:
    """Calculates body mass index (BMI)"""
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        print("Height cannot be equal to zero.")
        return None

def interpret_bmi(bmi: float)->str:
    """Interpretes BMI value according WHO classification."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "First-degree obesity"
    elif 35 <= bmi < 40:
        return "Second-degree obesity"
    else:
        return "Third-degree obesity"
    
def main() -> None:
    print("Body Mass Index (BMI) calculator")

    while True:
        print("\nMenu")
        print("Calculate BMI")
        print("Exit")

        choice = input("Choose action (1-2)").strip()

        if choice == "1":
            try:
                weight = float(input("Enter weight (kg): ").strip())
                height = float(input("Enter weight (kg): ").strip())

    
    
    