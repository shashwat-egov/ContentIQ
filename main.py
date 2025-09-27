from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", temperature=0)
react_prompt = hub.pull("hwchase17/react")
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=[
        "input",
        "tools",
        "tool_names",
        "agent_scratchpad",
        "format_instructions",
    ],
).partial(format_instructions=output_parser.get_format_instructions())

# Reasoning: The create_react_agent function creates an agent that can reason about which tool to use based on the input question and the available tools.
agent = create_react_agent(llm, tools, react_prompt_with_format_instructions)

# Runtime: The AgentExecutor is responsible for executing the agent's actions and managing the interaction between the agent and the tools.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
extract_output = RunnableLambda(lambda x: x["output"])
parse_output = RunnableLambda(lambda x: output_parser.parse(x))

chain = agent_executor | extract_output | parse_output


def main():
    result = chain.invoke(
        input={
            "input": "Find 3 trending and high-engagement topics in the fields of technology, AI, data engineering, and software development that professionals are currently discussing on Reddit. Focus on topics that are relevant for Senior Software Engineers and Technical Leads, and that would attract good visibility and engagement if written about. For each topic, provide a short explanation of why it is trending and suggest one possible angle for writing a LinkedIn post."
        }
    )
    print(result)


if __name__ == "__main__":
    main()
