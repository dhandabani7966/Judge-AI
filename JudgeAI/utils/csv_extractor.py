import pandas as pd

def extract_text_from_csv(uploaded_file):

    df = pd.read_csv(
        uploaded_file,
        nrows=5
    )

    for col in ["judgement", "judgment", "text", "content"]:

        if col in df.columns:

            return "\n\n".join(
                df[col].astype(str)
            )

    return "\n".join(
        df.astype(str)
        .fillna("")
        .agg(" ".join, axis=1)
    )