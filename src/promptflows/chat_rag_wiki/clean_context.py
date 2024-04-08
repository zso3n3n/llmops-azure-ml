from promptflow import tool
import re


@tool
def clean_context(context: str):
    # Use regex to replace all special characters with an empty string
    cleaned_string = re.sub(r"[^a-zA-Z0-9 ]", "", context)

    return cleaned_string