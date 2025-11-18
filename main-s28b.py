from dotenv import load_dotenv
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
 
 
load_dotenv()
 
 
tools = [TavilySearch(max_results=3, include_answer=False)]
llm = ChatOpenAI(model="gpt-4", temperature=0)

react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm=llm, 
    tools=tools, 
    prompt=react_prompt)
 
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor
 
def main():
    result = chain.invoke(
        {
            "input": "Search 1 job ppstings for an ai engineer using langchain on linkedin and list their details?",
        }
    )
    print(result)
 
 
if __name__ == "__main__":
    main()
