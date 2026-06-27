import nltk
import os

# Download NLTK data on startup
nltk_data_dir = os.path.expanduser("~/nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def generate_summary(text, sentence_count=5):
    """
    Generate an extractive summary from legal judgment text.
    """

    parser = PlaintextParser.from_string(
        text,
        Tokenizer("english")
    )

    summarizer = LsaSummarizer()

    summary = summarizer(
        parser.document,
        sentence_count
    )

    summary_text = " ".join(
        str(sentence)
        for sentence in summary
    )

    return summary_text


if __name__ == "__main__":

    sample_text = """
    The petitioner filed an appeal before the High Court seeking relief.
    The Court examined all the evidence carefully.
    After hearing both parties, the Court found that the trial court had committed an error.
    The appeal was allowed.
    The petitioner was granted relief.
    """

    print(generate_summary(sample_text))
