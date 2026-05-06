import pandas as pd
from src.utils import safe_divide

def compute_superstore_kpi(df):
    
     # Convert date column
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Create month column
    df["month"] = df["order_date"].dt.to_period("M")
    df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

    # Monthly aggregation
    monthly = df.groupby("month").agg(
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum"),
        total_orders=("order_id", "count")
    )
    return monthly

    #print(df.columns.tolist())
    #df["proc_lead_days"] = pd.to_numeric(df["proc_lead_days"], errors="coerce")

    #monthly = df.groupby("order_date").agg(
      #  orders=("order_id", "count"),
       # avg_lead_time=("proc_lead_days", "mean"),
        #lead_time_std=("proc_lead_days", "std"),
        #loss_rate=("profit", lambda x: (x < 0).mean()),
        #discount_rate=("discount", lambda x: (x > 0.2).mean()),
        #total_sales=("sales", "sum")
  #  ).reset_index()

    #daily = df.groupby(["ship_date", "order_date"])["order_id"].count().reset_index()

    #volatility = daily.groupby("order_date")["order_id"].agg(
       # lambda x: safe_divide(x.std(), x.mean())
#    ).reset_index(name="order_volatility")

   # monthly = monthly.merge(volatility, on="order_date", how="left")

    #return monthly