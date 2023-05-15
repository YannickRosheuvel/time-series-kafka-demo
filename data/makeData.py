# #!/usr/bin/env python

# """Make sample time series data.
# """
# import numpy as np
# import pandas as pd


# def main():
#     date_rng = pd.date_range(start='1/1/2021', end='1/2/2021', freq='s')
#     df = pd.DataFrame(date_rng, columns=['timestamp'])

#     np.random.seed(42)
#     df['value'] = np.random.randint(0, 100, size=(len(date_rng)))
#     df = df.sample(frac=0.5, random_state=42).sort_values(by=['timestamp'])
#     df.to_csv('data.csv', index=False)
#     return


# if __name__ == "__main__":
#     main()

import json
import numpy as np
import pandas as pd


def main():
    # Generate sample time series data
    date_rng = pd.date_range(start='1/1/2021', end='1/2/2021', freq='s')
    df = pd.DataFrame(date_rng, columns=['timestamp'])
    np.random.seed(42)
    df['value'] = np.random.randint(0, 100, size=(len(date_rng)))
    df = df.sample(frac=0.5, random_state=42).sort_values(by=['timestamp'])

    # Create sample data dictionary
    sample_data = {
        "userData": {
            "name": "Bella Beer",
            "roomNumber": "001"
        },
        "data": {
            "contractionData": {
                "0": {
                    "id": "Contractions",
                    "data": [
                        {
                            "x": str(df['timestamp'][0].time()),
                            "y": np.random.randint(10, 50)
                        }
                    ]
                }
            },
            "oxygenData": {
                "1": {
                    "id": "Oxygen Sat",
                    "data": [
                        {
                            "x": str(df['timestamp'][0].time()),
                            "y": np.random.randint(30, 100)
                        }
                    ]
                }
            },
            "heartRateData": {
                "2": {
                    "id": "Mother Heartrate",
                    "data": [
                        {
                            "x": str(df['timestamp'][0].time()),
                            "y": np.random.randint(50, 100)
                        }
                    ]
                },
                "3": {
                    "id": "Baby Heartrate",
                    "data": [
                        {
                            "x": str(df['timestamp'][len(df) - 1].time()),
                            "y": np.random.randint(100, 150)
                        }
                    ]
                }
            }
        }
    }

    # Save sample data to JSON file
    with open('sample_data.json', 'w') as f:
        json.dump(sample_data, f)

    return


if __name__ == "__main__":
    main()
