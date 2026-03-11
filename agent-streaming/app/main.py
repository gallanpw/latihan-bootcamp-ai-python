from app.tools import search_web
from app.llm import llm_model
from agents import Agent, Runner, set_tracing_disabled

set_tracing_disabled(True)


async def main():
    agent = Agent(
        "Assistant",
        instructions="You are helpful assistant.",
        model=llm_model,
        tools=[search_web],
    )
    runner = Runner.run_streamed(agent, input="Hey!")

    async for event in runner.stream_events():
        print(event)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
    # main()
