import pandas as pd
from src.utils import safe_divide

def compute_olist_kpi(df):

    df["delivery_days"] = pd.to_numeric(df["delivery_days"], errors="coerce")

    monthly = df.groupby("month").agg(
        orders=("order_id", "count"),
        avg_delivery_time=("delivery_days", "mean"),
        ontime_rate=("is_ontime", "mean"),
        cancel_rate=("is_cancelled", "mean")
    ).reset_index()

    daily = df.groupby(["month", "order_purchase_timestamp"])["order_id"].count().reset_index()

    volatility = daily.groupby("month")["order_id"].agg(
        lambda x: safe_divide(x.std(), x.mean())
    ).reset_index(name="order_volatility")

    monthly = monthly.merge(volatility, on="month", how="left")

    return monthly