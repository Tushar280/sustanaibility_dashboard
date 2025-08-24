import numpy as np

def zscore_anomalies(series: list[dict], threshold: float = 3.0):
    vals = np.array([p["value"] for p in series], dtype=float)
    if len(vals) < 10:
        return []
    mean = vals.mean()
    std = vals.std() or 1.0
    anomalies = []
    for i, p in enumerate(series):
        z = abs((p["value"] - mean) / std)
        if z >= threshold:
            anomalies.append({"ts": p["ts"], "value": p["value"], "z": float(z)})
    return anomalies
