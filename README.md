# Monte Carlo Retirement Simulator

A data science project that uses Monte Carlo simulation to model how an investment portfolio may perform over time under uncertain market conditions.

## 📌 Overview

This project simulates thousands of possible market scenarios using random sampling to estimate the future value of an investment portfolio. It helps visualize both expected returns and potential risks.

## ⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

## 🧠 How It Works

- Generates random yearly returns using a normal distribution
- Simulates portfolio growth over a fixed number of years
- Runs 10,000 simulations to represent different market outcomes
- Aggregates results to compute:
  - Median portfolio growth
  - 5th percentile (worst-case scenarios)
  - 95th percentile (best-case scenarios)

## 📊 Output

The project generates a **fan chart** showing:

- Median growth path (expected outcome)
- Confidence interval (risk range between 5% and 95%)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/monte-carlo-retirement.git
cd monte-carlo-retirement
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python main.py
```

## 📁 Project Structure

```
monte-carlo-retirement/
│── main.py
│── requirements.txt
│── README.md
│── results.png
```

## 📷 Example Output

After running the simulation, a chart like this will be generated:

- Median line represents expected portfolio growth
- Shaded region shows uncertainty (risk range)

## 🔧 Configuration

You can modify parameters in `main.py`:

| Parameter | Description |
|---|---|
| `initial_investment` | Starting portfolio value |
| `years` | Number of years to simulate |
| `mean_return` | Expected annual return rate |
| `volatility` | Standard deviation of returns |
| `simulations` | Number of Monte Carlo runs |

## 💡 Future Improvements

- Add user input (CLI or web form)
- Export results to CSV
- Build a web dashboard (Flask / React)
- Deploy as an API

## 🎯 Use Cases

- Financial forecasting
- Risk analysis
- Investment planning
- Data science portfolio project

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Your Name** — GitHub: [your-username](https://github.com/your-username)
