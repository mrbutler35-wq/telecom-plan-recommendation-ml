import pandas as pd

def test_load_dataset():
    df = pd.read_csv('users_behavior.csv')
    assert not df.empty
