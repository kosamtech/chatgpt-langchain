from langchain.chat_models.openai import ChatOpenAI


def build_llm(chat_args):
    return ChatOpenAI(
        streaming=chat_args.streaming
    )
