import pandas as pd
import numpy as np
newdf=pd.DataFrame(np.random.rand(500,6))
# print(newdf) // data frame

newSer=pd.Series(np.random.rand(34))
# print(newSer)
print(type(newSer))

# datatype
print(newSer.dtype)

print(newSer.head(10))
print(newSer.index)
print(newdf.columns)
print(newdf.to_numpy())
