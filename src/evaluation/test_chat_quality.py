from promptflow.client import PFClient


def quality_test(): 
  # PFClient can help manage your runs and connections.
  pf = PFClient()

  # Define Flows and Data
  chat_flow = "./src/promptflows/chat_rag_wiki" # set the flow directory
  eval_flow = "./src/evaluation/eval_flow" # set flow directory
  data = "./src/evaluation/input_test_data.csv" # set the data file

  # Run chat flow to generate chat results
  rag_chat_run = pf.run(
      flow=chat_flow,
      data=data,
      stream=False,
      column_mapping={  # map the url field from the data to the url input of the flow
        "input": "${data.input}",
      }
  )

  # Run evaluation flow to evaluate chat results
  rag_eval_run = pf.run(
      flow=eval_flow,
      data=data,
      run=rag_chat_run,
      stream=False,
      column_mapping={  # map the url field from the data to the url input of the flow
        "question": "${data.input}",
        "answer": "${run.outputs.answer}",
        "context": "${run.outputs.context}"
      }
  )

  metric_dict = dict(pf.get_metrics(rag_eval_run))

  print(f"RESULTS: {metric_dict}")

  assert(metric_dict['fluency'] >= 5)
  assert(metric_dict['answer_context_sim'] >= 0.97)
  assert(metric_dict['groundedness'] >= 5)

  return metric_dict

if __name__ == "__main__":
  quality_test()  