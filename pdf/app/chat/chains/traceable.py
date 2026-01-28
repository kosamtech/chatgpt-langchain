from langfuse.model import CreateTrace
from app.chat.tracing.langfuse import langfuse

from typing import Any


class TraceableChain:
    def __call__(self, *args: Any, **kwargs: Any):
        trace = langfuse.trace(
            CreateTrace(
                id=self.metadata['conversation_id'],
                metadata=self.metadata
            )
        )
        callbacks = kwargs.get("callbacks", [])
        callbacks.append(trace.getNewHandler())
        kwargs["callbacks"] = callbacks

        return super().__call__(*args, **kwargs)