def estimate(x, t, v):
    time_needed = x / v * 60
    return "Yes" if time_needed <= t else "No"