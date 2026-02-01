import pandas as pd
data = {
    "time":[1,2,3,4,5],
    "Value": [10,None,30,None,50]
}

df = pd.DataFrame(data)
print("Befor interpolation")
print(df)

print()

df['Value'] = df['Value'].interpolate(method="linear")
print("After interpolation")
print(df)


'''
When to use interpolation
1. time series data -> like stock market data
2. Numeric data who follow trends
3. avoid dropping rows
'''