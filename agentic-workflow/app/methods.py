# -> User Input a Topic
# -> Generate sets of Queries
# -> Each query going to search to the web
# -> Summarize the results
# -> Generate Report
import json
from app.utils import oa_client, tavily_client
from app.schema import QueriesSchema
# import logging

# logger = logging.getLogger(__name__)


def generate_queries(topic: str) -> QueriesSchema:
    response = oa_client.chat.completions.parse(
        model="google/gemini-3-flash-preview",
        messages=[
            {
                "role": "system",
                "content": "Generate 5 queries to search into the web based on user topic",
            },
            {"role": "user", "content": f"topic: {topic}"},
        ],
        response_format=QueriesSchema,
    )

    if not response:
        raise ValueError("No response from OpenAI")

    parsed_data = response.choices[0].message.parsed.model_dump()  # type: ignore
    # logger.info(f"Generated queries: {parsed_data}")
    print(f"Generated queries: {parsed_data}")

    return QueriesSchema(**parsed_data)


def search_web(query: str) -> str:
    result = tavily_client.search(
        query=query, search_depth="advanced", include_raw_content="markdown"
    )
    # logger.info(f"Search result: {result}")
    print(f"Search result: {result}")

    response = oa_client.chat.completions.create(
        model="deepseek/deepseek-v3.2-exp",
        messages=[
            {
                "role": "system",
                # "content": "Generate 5 queries to search into the web based on user topic",
                "content": "Sumarize this into informative content, please include date, numbers and url/sources",
            },
            {"role": "user", "content": f"Search Result: {json.dumps(result)}"},
        ],
        extra_body={"reasoning": {"enabled": True}},
    )

    return response.choices[0].message.content  # type: ignore
