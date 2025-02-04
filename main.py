import Agent
import secret
import json
import outscraper
import logging

outscraper.export_last_month_reviews(secret.get_outscraper_api_key(),secret.get_customer_placeid())

with open("prompts.json", "r") as f:
    prompts = json.load(f)

#agent = Agent.DocumentQueryEngine(secret.get_openai_api_key())
logging.info("Fetching reviews...")
"""
query_agent = agent.get_router_query_engine(
    "avaliacoes.json",
    summary_tool_description=prompts["main"]["summary_tool_description"],
    vector_tool_description=prompts["main"]["vector_tool_description"],
    sys_prompt=prompts["main"]["sys_prompt"]
    )
"""

query_agent = Agent.initialize_query_engine(secret.get_openai_api_key(),"avaliacoes.json",prompts["main"])

while(1):
    print('\nVoce: ', end='')
    question = str(input(''))
    print()
    print("Seu agente de IA: ",query_agent.query(question))