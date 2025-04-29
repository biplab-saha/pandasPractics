Step 2: Use full or relative path correctly
If the file is in another directory, you can give the full path in your Python script like this:
file = pd.read_csv(r"C:\Users\biplap\Desktop\Code\Pandas\pandasPractics\sales_data.csv")

Or, if it’s in the parent directory, you can go up one level with ..:
file = pd.read_csv("../sales_data.csv")

Step 3: Check for typos
Make sure:
The filename is exactly sales_data.csv (check for .CSV, spaces, etc.).
There are no hidden file extensions like sales_data.csv.txt.
