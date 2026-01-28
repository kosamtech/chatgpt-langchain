import argparse
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain

parser = argparse.ArgumentParser()
parser.add_argument("--task", "-t", default="return  a list of numbers")
parser.add_argument("--language", "-l", default="python")
args = parser.parse_args()

llm = OpenAI()

code_prompt = PromptTemplate(
  template="Write a very short {language} function that will {task}",
  input_variables=["language", "task"]
)

code_test = PromptTemplate(
  template="Write a test for the following {language} code: \n {code}",
  input_variables=["language", "code"]
)

code_chain = LLMChain(
  llm=llm,
  prompt=code_prompt,
  output_key="code"
)

test_chain = LLMChain(
  llm=llm,
  prompt=code_test,
  output_key="test"
)

chain = SequentialChain(
  chains=[code_chain, test_chain],
  input_variables=["task", "language"],
  output_variables=["test", "code"]
)

result = chain({
  "language": args.language,
  "task": args.task
})

print(result)

if __name__ == "__main__":
  # main()
  pass