import pandas as pd

def test_load_dataset():
    df = pd.read_csv('data/raw/users_behavior.csv')
    assert not df.empty
