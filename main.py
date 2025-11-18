from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch



tools = [TavilySearch(max_results=3, include_answer=False)]
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

react_prompt= hub.pull("hwchase17/react")
agent = create_react_agent(
   llm=llm,
   tools=tools,
   prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)
chain = agent_executor

def main():
   result = chain.invoke(
       {
           "input": "Search 3 job ppstings for an ai engineer using langchain on linkedin and list their details?",
       }
   )
   print(result)
if __name__ == "__main__":
   main()
