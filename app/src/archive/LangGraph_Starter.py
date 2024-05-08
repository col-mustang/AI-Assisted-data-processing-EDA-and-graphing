from typing import TypedDict, List
import colorama
import os
from dotenv import load_dotenv, find_dotenv


from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

from langgraph.graph import StateGraph, END
from langgraph.pregel import GraphRecursionError

from langchain_openai import ChatOpenAI


# Define the paths.
search_path = os.path.join(os.getcwd(), "app")
print(f"the search path is {search_path}")
code_file = os.path.join(search_path,"src\\crud.py")
test_file = os.path.join(search_path, "test\\test_crud.py")

# # Create the folders and files if necessary.
# if not os.path.exists(search_path):
#     os.mkdir(search_path)
#     os.mkdir(os.path.join(search_path, "src"))
#     os.mkdir(os.path.join(search_path, "test"))

load_dotenv(find_dotenv())

together_api_key = os.environ.get("TOGETHER_API_KEY")
print(together_api_key)

llm = ChatOpenAI(base_url="https://api.together.xyz/v1",
    api_key=together_api_key,
    model="deepseek-ai/deepseek-coder-33b-instruct")

class AgentState(TypedDict):
    class_source: str
    class_methods: List[str]
    tests_source: str

# Create the graph.
workflow = StateGraph(AgentState)

def extract_code_from_message(message):
    lines = message.split("\n")
    code = ""
    in_code = False
    for line in lines:
        if "```" in line:
            in_code = not in_code
        elif in_code:
            code += line + "\n"
    return code

import_prompt_template = """Here is a path of a file with code: {code_file}.
Here is the path of a file with tests: {test_file}.
Write a proper import statement for the class in the file.
"""
# Discover the class and its methods.
def discover_function(state: AgentState):
    assert os.path.exists(code_file)
    with open(code_file, "r") as f:
        source = f.read()
    state["class_source"] = source

    # Get the methods.
    methods = []
    for line in source.split("\n"):
        if "def " in line:
            methods.append(line.split("def ")[1].split("(")[0])
    state["class_methods"] = methods

    # Generate the import statement and start the code.
    import_prompt = import_prompt_template.format(
        code_file=code_file,
        test_file=test_file
    )
    message = llm.invoke([HumanMessage(content=import_prompt)]).content
    code = extract_code_from_message(message)
    state["tests_source"] = code + "\n\n"

    return state


# Add a node to for discovery.
workflow.add_node(
    "discover",
    discover_function
)

system_message_template = """You are a smart developer. You will write unit 
tests that have a high quality. Use pytest.

Reply with the source code for the test only. 
Do not include the class in your response. I will add the imports myself.
If there is no test to write, reply with "# No test to write" and 
nothing more. Do not include the class in your response.

Example:

```
def test_function():
    ...
```


Do not write test classes, only methods.
"""

# Write the tests template.
write_test_template = """Here is a class:
'''
{class_source}
'''

Implement a test for the method \"{class_method}\".
"""

# This method will write a test.
def write_tests_function(state: AgentState):

    # Get the next method to write a test for.
    class_method = state["class_methods"].pop(0)
    print(f"Writing test for {class_method}.")

    # Get the source code.
    class_source = state["class_source"]

    # Create the prompt.
    write_test_prompt = write_test_template.format(
        class_source=class_source,
        class_method=class_method
    )
    print(colorama.Fore.CYAN + write_test_prompt + colorama.Style.RESET_ALL)

    # Get the test source code.
    system_message = SystemMessage(system_message_template)
    human_message = HumanMessage(write_test_prompt)
    test_source = llm.invoke([system_message, human_message]).content
    test_source = extract_code_from_message(test_source)
    print(colorama.Fore.GREEN + test_source + colorama.Style.RESET_ALL)
    state["tests_source"] += test_source + "\n\n"

    return state

# Add the node.
workflow.add_node(
    "write_tests",
    write_tests_function
)

# Define the entry point. This is where the flow will start.
workflow.set_entry_point("discover")

# Always go from discover to write_tests.
workflow.add_edge("discover", "write_tests")

# Write the file.
def write_file(state: AgentState):
    with open(test_file, "w") as f:
        f.write(state["tests_source"])
    return state

# Add a node to write the file.
workflow.add_node(
    "write_file",
    write_file)

# Find out if we are done.
def should_continue(state: AgentState):
    if len(state["class_methods"]) == 0:
        return "end"
    else:
        return "continue"

# Add the conditional edge.
workflow.add_conditional_edges(
    "write_tests",
    should_continue,
    {
        "continue": "write_tests",
        "end": "write_file"
    }
)

# Always go from write_file to end.
workflow.add_edge("write_file", END)

# Create the app and run it
app = workflow.compile()
inputs = {}
config = RunnableConfig(recursion_limit=100)
try:
    result = app.invoke(inputs, config)
    print(result)
except GraphRecursionError:
    print("Graph recursion limit reached.")



