from pydantic import BaseModel, ConfigDict, Field, field_validator


class QueryRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(
        min_length=1,
        max_length=10_000,
        description="The user's query.",
    )

    use_cache: bool = Field(
        default=True,
        description="Whether semantic caching is enabled for this request.",
    )

    @field_validator("query")
    @classmethod
    def validate_query(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Query cannot contain only whitespace.")

        return value
