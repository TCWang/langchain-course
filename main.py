from dotenv import load_dotenv
from langchain import hub # ✅ updated import
from langchain.agents.react import create_react_agent
from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
 
 
load_dotenv()
 
 
tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", temperature=0)
 
react_prompt= hub.pull("hwchase17/react")
agent = create_react_agent(
    llm=llm, 
    tools=tools, 
    prompt=react_prompt)
 
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
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