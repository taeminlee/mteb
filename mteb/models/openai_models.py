from __future__ import annotations

import logging
from functools import partial
from typing import Any

import numpy as np
import tqdm

from mteb.model_meta import ModelMeta
from mteb.models.text_formatting_utils import corpus_to_texts
from mteb.requires_package import requires_package

import tiktoken

logger = logging.getLogger(__name__)


class OpenAIWrapper:
    def __init__(self, model_name: str, embed_dim: int | None = None, **kwargs) -> None:
        requires_package(self, "openai", "Openai text embedding")
        from openai import OpenAI

        self._client = OpenAI()
        self._model_name = model_name
        self._embed_dim = embed_dim
        self.enc = tiktoken.encoding_for_model(model_name)
    
    def truncate(self, sentence, max_length=8192, pass_length=1024):
        if len(sentence) < pass_length:
            return sentence
        return self.enc.decode(self.enc.encode(sentence)[0:max_length])

    def encode(self, sentences: list[str], **kwargs: Any) -> np.ndarray:
        requires_package(self, "openai", "Openai text embedding")
        requires_package(self, "tiktoken", "Openai tokenizer")
        minibatch_size = 64
        embeds = []
        for i in tqdm.tqdm(range(0, len(sentences), minibatch_size)):
            minibatch = sentences[i:i+minibatch_size]
            minibatch = [self.truncate(sentence) for sentence in minibatch]
            from openai import NotGiven

            if self._model_name == "text-embedding-ada-002" and self._embed_dim is not None:
                logger.warning(
                    "Reducing embedding size available only for text-embedding-3-* models"
                )

            embeds += [e.embedding for e in 
                       self._client.embeddings.create(
                            input=minibatch,
                            model=self._model_name,
                            encoding_format="float",
                            dimensions=self._embed_dim or NotGiven()).data]
            
        return np.array(embeds)

    def encode_queries(self, queries: list[str], **kwargs: Any) -> np.ndarray:
        return self.encode(queries, **kwargs)

    def encode_corpus(
        self, corpus: list[dict[str, str]] | dict[str, list[str]], **kwargs: Any
    ) -> np.ndarray:
        sentences = corpus_to_texts(corpus)
        return self.encode(sentences, **kwargs)



text_embedding_3_small = ModelMeta(
    name="text-embedding-3-small",
    revision="1",
    release_date="2024-01-25",
    languages=None,  # supported languages not specified
    loader=partial(OpenAIWrapper, model_name="text-embedding-3-small"),
    max_tokens=8191,
    embed_dim=1536,
    open_source=False,
)
text_embedding_3_large = ModelMeta(
    name="text-embedding-3-large",
    revision="1",
    release_date="2024-01-25",
    languages=None,  # supported languages not specified
    loader=partial(OpenAIWrapper, model_name="text-embedding-3-large"),
    max_tokens=8191,
    embed_dim=3072,
    open_source=False,
)
text_embedding_ada_002 = ModelMeta(
    name="text-embedding-ada-002",
    revision="1",
    release_date="2022-12-15",
    languages=None,  # supported languages not specified
    loader=partial(OpenAIWrapper, model_name="text-embedding-ada-002"),
    max_tokens=8191,
    embed_dim=1536,
    open_source=False,
)
