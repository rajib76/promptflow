import os
from promptflow.core import tool
from dotenv import load_dotenv
from trulens_eval.feedback import Groundedness
from trulens_eval.feedback.provider.openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
openai_provider = OpenAI()


@tool
def get_score(source: str, statement: str):
    groundedness_imp = Groundedness(groundedness_provider=openai_provider)
    result = groundedness_imp.groundedness_measure_with_cot_reasons(source=source, statement=statement)
    score = result[0]["statement_0"]
    return float(score)
