import pandas as pd
import numpy as np
df = pd.DataFrame()
data = pd.DataFrame({"col1": range(3),"col2": range(3)})
print("After appending some data:")
df = df.append(data)
print(df)
