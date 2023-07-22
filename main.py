import polars


df = polars.read_parquet("./data/NTLHNew.parquet")

print(df.filter(polars.col("livro") == "1%20João"))

df2 = polars.read_parquet("./data/ARCNew.parquet")


print(df2.filter(polars.col("livro") == "1%20João"))
