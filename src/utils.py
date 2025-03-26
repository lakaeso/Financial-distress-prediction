# hiperparam search

# print acc and score and etc ...

# remove top quantile
def remove_top_quantile(df, column_name, quantile):
    quantile_filter = df[column_name] < df[column_name].quantile(quantile)
    
    return df[quantile_filter]