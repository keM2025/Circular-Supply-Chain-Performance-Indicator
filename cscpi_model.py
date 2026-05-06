from src.utils import min_max_normalize, invert
import pandas as pd

def compute_cscpi(superstore_kpi, olist_kpi):

    df = pd.merge(superstore_kpi, olist_kpi, on="order_date", suffixes=("_s", "_o"))

    # Normalize and invert scores so that higher is better for all metrics
    df["lead_time_score"] = invert(min_max_normalize(df["avg_lead_time"]))
    df["delivery_score"] = invert(min_max_normalize(df["avg_delivery_time"]))
    df["loss_score"] = invert(min_max_normalize(df["loss_rate"]))
    df["cancel_score"] = invert(min_max_normalize(df["cancel_rate"]))
    df["volatility_score"] = invert(min_max_normalize(df["order_volatility_s"]))

    # Dimension scores
    df["operational_score"] = (df["lead_time_score"] + df["delivery_score"]) / 2
    df["circular_score"] = (df["loss_score"] + df["cancel_score"]) / 2
    df["resilience_score"] = df["volatility_score"]

    # --- Final CSCPI ---
    df["CSCPI"] = (
        0.4 * df["operational_score"] +
        0.3 * df["circular_score"] +
        0.3 * df["resilience_score"]
    )

    return df