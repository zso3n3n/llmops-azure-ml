from promptflow import tool
from typing import List
from statistics import mean
# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def aggregate_results(results: List[dict]) -> dict:


    fluency_scores = [result['fluency'] for result in results]
    groundedness_scores = [result['groundedness'] for result in results]
    answer_context_sim_scores = [result['answer_context_sim'] for result in results]

    output = {
        'fluency': mean(fluency_scores),
        'groundedness': mean(groundedness_scores),
        'answer_context_sim': round(mean(answer_context_sim_scores),2)
    }

    return output


if __name__ == "__main__":

    input_dict = [{'fluency': 1, 'groundedness': 1, 'answer_context_sim': 1},{'fluency': 2, 'groundedness': 2, 'answer_context_sim': 2}]
    aggregate_results(input_dict)