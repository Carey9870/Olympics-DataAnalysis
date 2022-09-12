import pandas as pd

def preprocess(ath_events, noc_reg):
    # merging
    df = ath_events.merge(noc_reg, on='NOC', how='left')
    # drop duplicates
    df.drop_duplicates(inplace=True)
    # one-hot encoding of medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df