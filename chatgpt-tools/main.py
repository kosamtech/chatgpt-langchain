from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.schema import SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from dotenv import load_dotenv

from .sql import run_query_tool, list_tables, describe_table_tool
from .report import write_report_tool
from .chat_model_start_handler import ChartModelStartHandler



load_dotenv()


handler = ChartModelStartHandler()
chat = ChatOpenAI(callbacks=[handler])

tables = list_tables()
prompt = ChatPromptTemplate(
    messages= [
        SystemMessage(content=(
          "You are an AI that has access to a SQLite database.\n"
          f"The database has the following tables: {tables} \n"
          "Do not make any assumptions about what tables exist "
          "or what columns exist. Instead, use the `describe_tables` function"
        )),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") # `agent_scratchpad` is a special name
    ]
)


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [run_query_tool, describe_table_tool, write_report_tool]

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
    memory=memory
)

agent_executor("How many users are in the database?")