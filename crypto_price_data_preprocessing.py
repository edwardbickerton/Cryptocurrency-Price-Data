#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:08:37 2023

@author: edwardbickerton
"""
import pandas as pd


def read_crypto(symbol, name):
    return pd.read_csv(
        "archive/Price-Data/" +
        "_".join([symbol, name]) + ".csv",
        usecols=["Date", "Open"]
    ).rename(columns={"Open": symbol})


index_df = pd.read_csv(
    "archive/Index/Index.csv",
    index_col=0
)
crypto_dfs = []
crypto_symbols = []
for idx, row in index_df.iterrows():
    crypto_symbols.append(row["Symbol"])
    crypto_dfs.append(read_crypto(row["Symbol"], row["Name"]))

crypto_price_data = crypto_dfs[0]
for df in crypto_dfs[1:]:
    crypto_price_data = crypto_price_data.merge(df, on="Date", how="outer")

crypto_price_data.to_csv("cryptocurrency_daily_open.csv")
