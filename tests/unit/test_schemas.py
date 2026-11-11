import pytest
from pydantic import ValidationError

from smartllm_gateway.core.schemas import QueryRequest


def test_valid_query_request():
    request = QueryRequest(query="Explain semantic caching")

    assert request.query == "Explain semantic caching"
    assert request.use_cache is True


def test_query_whitespace_is_removed():
    request = QueryRequest(query="  Hello world  ")

    assert request.query == "Hello world"


def test_empty_query_is_rejected():
    with pytest.raises(ValidationError):
        QueryRequest(query="")


def test_whitespace_only_query_is_rejected():
    with pytest.raises(ValidationError):
        QueryRequest(query="     ")


def test_unexpected_fields_are_rejected():
    with pytest.raises(ValidationError):
        QueryRequest(
            query="Hello",
            admin=True,
        )


def test_cache_can_be_disabled():
    request = QueryRequest(
        query="Explain RAG",
        use_cache=False,
    )

    assert request.use_cache is False
