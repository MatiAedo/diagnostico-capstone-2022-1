def top_days(data):
    out = data['date'].dt.date.value_counts().head(10)
    return out
