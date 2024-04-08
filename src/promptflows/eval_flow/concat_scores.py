from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def concat_scores(question: str, answer: str, context: str, groundedness: str, fluency_score: str, answer_context_sim: float) -> dict:

    output_json = {'question': question,
                   'answer': answer,
                   'context': context,
                   'fluency' : int(fluency_score),
                   'groundedness': int(groundedness),
                   'answer_context_sim' : answer_context_sim
                   }
    
    return output_json
