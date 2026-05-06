import matplotlib.pyplot as plt
from src.config import OUTPUT_FIGURES

def plot_cscpi(df):

    plt.figure()

    plt.plot(df["order_date"], df["CSCPI"])
    plt.xticks(rotation=45)

    plt.title("CSCPI Trend Over Time")
    plt.xlabel("Month")
    plt.ylabel("CSCPI Score")

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FIGURES}cscpi_trend.png")

    plt.show()