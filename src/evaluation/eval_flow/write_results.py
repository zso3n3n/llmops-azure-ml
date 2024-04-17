from promptflow.core import tool
from typing import List
import json

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def write_results(results: List[dict]) -> bool:

   with open ('../../../../data/outputs/rag_eval_results.json', 'w') as fout:
      json.dump(results, fout)

   return 0
