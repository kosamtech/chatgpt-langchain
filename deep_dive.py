from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory, ConversationSummaryMemory

prompt = ChatPromptTemplate(
  input_variables=["content", "messages"],
  messages = [
    MessagesPlaceholder(variable_name="messages"),
    HumanMessagePromptTemplate.from_template("{content}")
  ]
)

chat = ChatOpenAI()

# memory = ConversationBufferMemory(
#   memory_key="messages",
#   return_messages=True,
#   chat_memory=FileChatMessageHistory("messages.json"),
# )

memory = ConversationSummaryMemory(
  memory_key="messages",
  return_messages=True,
  llm=chat
)

chain = LLMChain(
  llm=chat,
  prompt=prompt,
  memory=memory
)

while True:
  content = input(">> ")

  result = chain({"content": content})

  print(result.text)