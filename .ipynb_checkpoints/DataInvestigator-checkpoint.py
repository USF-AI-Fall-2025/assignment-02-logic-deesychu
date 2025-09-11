# Author: Adrienne Dominique Sy Chu

import pandas as pd

class DataInvestigator:
    def __init__(self, df: pd.DataFrame):
        # Constructor: takes in a pandas DataFrame. If invalid, sets an error flag.
        if isinstance(df, pd.DataFrame):
            self.df = df
            self.error = False
        else:
            self.df = None
            self.error = True

    def baseline(self, col: int):
        # Returns the most frequent value in the column (zero-indexed). If error state is active, return None.
        if self.error:
            return None
        try:
            return self.df.iloc[:, col].mode().iloc[0]
        except Exception:
            return None

    def corr(self, col1: int, col2: int):
        # Returns the linear correlation between two columns. If error state is active, return None.
        if self.error:
            return None
        try:
            return self.df.iloc[:, col1].corr(self.df.iloc[:, col2])
        except Exception:
            return None

    def zeroR(self, col: int):
        # Returns the most frequent value in the column (same as baseline). If error state is active, return None.
        return self.baseline(col)

