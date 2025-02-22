import pandas as pd

class CoolingLoadCalculator:
    WATER_DENSITY = 1006  # kg/m³ (Corrected as per your formula)
    SPECIFIC_HEAT_CAPACITY = 4.1910  # kJ/kg·K (Corrected as per your formula)

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.data = None

    def load_data(self):
        """Loads CSV data and cleans column names."""
        self.data = pd.read_csv(self.input_file, encoding="utf-8-sig")

        # Fix column names (remove extra spaces)
        self.data.columns = self.data.columns.str.strip()

        # Convert necessary columns to float
        self.data["Supply Temp."] = pd.to_numeric(self.data["Supply Temp."], errors="coerce")
        self.data["Return Temp."] = pd.to_numeric(self.data["Return Temp."], errors="coerce")
        self.data["Flow Rate."] = pd.to_numeric(self.data["Flow Rate."], errors="coerce")

    def calculate_cooling_load(self):
        """Calculates Flow Rate in kg/s and Cooling Load in kW."""
        
        self.data["Flow Rate (kg/s)"] = (self.data["Flow Rate."] * self.WATER_DENSITY) / 60
        self.data["Cooling Load (kW)"] = (
            (self.data["Return Temp."] - self.data["Supply Temp."]) *
            self.data["Flow Rate (kg/s)"] *
            self.SPECIFIC_HEAT_CAPACITY
        )  

    def save_data(self):
        """Saves the processed data in CSV format, ready for Excel."""
        self.data.to_csv(self.output_file, index=False, encoding="utf-8-sig")

# File Paths
input_csv = "SampleData.csv"   # Change this to your actual input file
output_csv = "processed_data.csv"  # Output file for Excel

# Run the program
calculator = CoolingLoadCalculator(input_csv, output_csv)
calculator.load_data()
calculator.calculate_cooling_load()
calculator.save_data()

print(f"Processed data saved to {output_csv}")
