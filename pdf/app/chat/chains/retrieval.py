from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain
from app.chat.chains.traceable import TraceableChain


class StreamingConversationalRetrievalChain(
  TraceableChain, StreamableChain, ConversationalRetrievalChain
):
    pass
