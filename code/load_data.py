import pandas as pd
import os
from pathlib import Path


def load_bill_data():
    bill_df = pd.DataFrame(columns=["file_name", "file_text"])
    data_path = os.getenv("WRITE_BILLS_PATH", "../data/final_data/bills/")
    dirpath = Path(data_path)

    for filename in dirpath.iterdir():
        file_text = filename.read_text()
        bill_df = bill_df.append(
            {"file_name": filename.name, "file_text": file_text}, ignore_index=True
        )

    return bill_df
