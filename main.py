from src.load_validate import load_data
from src.superstore_kpi import compute_superstore_kpi
from src.olist_kpi import compute_olist_kpi
from src.cscpi_model import compute_cscpi
from src.visualisation import plot_cscpi

def main():

    superstore, olist = load_data()

    super_kpi = compute_superstore_kpi(superstore)
    olist_kpi = compute_olist_kpi(olist)

    cscpi_df = compute_cscpi(super_kpi, olist_kpi)

    print(cscpi_df.head())

    plot_cscpi(cscpi_df)

if __name__ == "__main__":
    main()