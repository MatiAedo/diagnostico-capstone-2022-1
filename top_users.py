def top_users(data):
    # Basado en: https://re-thought.com/pandas-value_counts/ para contar las apariciones del usuario por medio de
    # una función lambda para acceder al username
    out = data['user'].apply(lambda x: x['username']).value_counts().head(10)
    return out