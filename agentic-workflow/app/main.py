# Simple Deep Research
# -> User Input a Topic
# -> Generate sets of Queries
# -> Each query going to search to the web
# -> Summarize the results
# -> Generate Report

# import logging
from app.methods import generate_queries, search_web

# logger = logging.getLogger(__name__)


def main():

    research_context = ""
    # logger.info("Starting workflow...")
    queries = generate_queries("Entry Level Jobs risk in AI Era")
    print(queries.queries)
    for query in queries.queries[:1]:
        result = search_web(query)
        research_context = f"Query: {query} \n\n Result: {result} \n\n"

    with open("research_context.txt", "w") as f:
        f.write(research_context)


if __name__ == "__main__":
    main()
