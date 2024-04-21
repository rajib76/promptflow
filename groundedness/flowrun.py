from promptflow.client import PFClient
# from promptflow.entities import Run

# Get a pf client to manage runs
pf = PFClient()

# # Initialize an Run object
# run = Run(
#     flow="/Users/joyeed/promptflow/promptflow/groundedness/flow.dag.yaml",
#     # run flow against local data or existing run, only one of data & run can be specified.
#     data="/Users/joyeed/promptflow/promptflow/groundedness/data.jsonl",
#     column_mapping={"source": "${data.source}","statement": "${data.statement}"},
# )

inputs = [{"source": "TajMahal is a monument is Agra. it is situated in the bank of Yamuna","statement":"TajMahal is in the bank of Yanuma"},
          {"source": "Eiffel Tower is a iron tower and it is in Paris, France","statement":"Eiffel tower is made of iron"}]

for input in inputs:
    source = input["source"]
    statement = input["statement"]
    result = pf.test(flow="/Users/joyeed/promptflow/promptflow/groundedness/flow.dag.yaml",inputs={"source":source,"statement":statement})
    print(result)
# Create the run

# result = pf.runs.create_or_update(run,stream=False)
# print(result)