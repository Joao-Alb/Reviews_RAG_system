import Agent
import secret
import json
import outscraper

outscraper.export_last_month_reviews(secret.get_outscraper_api_key(),secret.get_customer_placeid())

with open("prompts.json", "r") as f:
    prompts = json.load(f)

agent = Agent.DocumentQueryEngine(secret.get_openai_api_key())

query_agent = agent.get_router_query_engine(
    "avaliacoes.json",
    summary_tool_description=prompts["summary_tool_description"],
    vector_tool_description=prompts["vector_tool_description"],
    sys_prompt=prompts["sys_prompt"]
    )

while(1):
    print('\nVoce: ', end='')
    question = str(input(''))
    print()
    print("Seu agente de IA: ",query_agent.query(question))