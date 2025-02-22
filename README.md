# Cooling Load Calculator

## Overview
This project calculates cooling loads from temperature and flow rate data stored in a CSV file. It filters data where chillers are ON, computes the average cooling load, and saves the processed results to a new CSV file.

## Features
- Reads and cleans CSV data
- Computes flow rate in kg/s
- Calculates cooling load in kW
- Filters and computes the average cooling load when the chiller is ON
- Saves the processed data and displays it on the console

## Formula Used
- **Flow Rate (kg/s):**  
  \[ \text{Flow Rate (kg/s)} = \frac{\text{Flow Rate (l/min)} \times 1006}{60} \]

- **Cooling Load (kW):**  
  \[ \text{Cooling Load} = (\text{Return Temp} - \text{Supply Temp}) \times \text{Flow Rate (kg/s)} \times 4.1910 \]

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Root2365/CoolingLoad-python.git
   cd cooling-load-calculator
   ```
2. Install dependencies (if needed):
   ```sh
   pip install pandas
   ```

## Usage
1. Place your input CSV file (e.g., `SampleData.csv`) in the project directory.
2. Run the script:
   ```sh
   python cooling_load_calculator.py
   ```
3. The processed data will be saved as `processed_data.csv`, and results will be displayed on the console.

## File Structure
```
 cooling-load-calculator/
 ├── sample_data.csv       # Input data file (replace with your own)
 ├── cooling_load_calculator.py  # Main Python script
 ├── README.md             # Project documentation
 ```

## Example Output
```sh
Average Cooling Load when Chiller is ON: 15.78 kW
Processed Data:
       Chiller Status  Supply Temp.  Return Temp.  Flow Rate (kg/s)  Cooling Load (kW)
0                1         6.1          13.4             32.1             120.45
1                1         6.2          14.3             32.0             125.78
...
```

