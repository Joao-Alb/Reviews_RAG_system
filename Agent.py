from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import SummaryIndex, VectorStoreIndex
from llama_index.core.tools import QueryEngineTool
from llama_index.core.query_engine.router_query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector

gpt_model = "gpt-4o-mini-2024-07-18"
embed_model_gpt = "text-embedding-ada-002"

def initialize_query_engine(api_key, documents_path, prompts):
    agent = DocumentQueryEngine(api_key)
    return agent.get_router_query_engine(
        documents_path,
        summary_tool_description=prompts["summary_tool_description"],
        vector_tool_description=prompts["vector_tool_description"],
        sys_prompt=prompts["sys_prompt"]
    )

class DocumentQueryEngine():
    
    def __init__(self,key):
        OpenAI.api_key = key

    def __get_documents(self,documents_path):
        return SimpleDirectoryReader(input_files=[documents_path]).load_data()

    def get_router_query_engine(self,documents_path: str, llm = None, embed_model = None, 
                                summary_tool_description = "Useful for summarization questions related to the documents.",
                                vector_tool_description = "Useful for retrieving specific context from the documents.",
                                sys_prompt=""):
        llm = llm or OpenAI(model=gpt_model)
        embed_model = embed_model or OpenAIEmbedding(model=embed_model_gpt)

        documents = self.__get_documents(documents_path)
        
        splitter = SentenceSplitter(chunk_size=1024)
        nodes = splitter.get_nodes_from_documents(documents)
        
        summary_index = SummaryIndex(nodes)
        vector_index = VectorStoreIndex(nodes, embed_model=embed_model)
        
        summary_query_engine = summary_index.as_query_engine(
            response_mode="tree_summarize",
            use_async=True,
            llm=llm
        )
        vector_query_engine = vector_index.as_query_engine(llm=llm)
        
        summary_tool = QueryEngineTool.from_defaults(
            query_engine=summary_query_engine,
            description=(
                summary_tool_description
            ),
        )
        
        vector_tool = QueryEngineTool.from_defaults(
            query_engine=vector_query_engine,
            description=(
                vector_tool_description
            ),
        )
        
        query_engine = RouterQueryEngine(
            selector=LLMSingleSelector.from_defaults(),
            query_engine_tools=[
                summary_tool,
                vector_tool,
            ],
            verbose=False
        )
        return query_engine

class QueryEngine(RouterQueryEngine):
    context = []

    def __init__(self, selector, query_engine_tools, llm = None, summarizer = None, verbose = False,sys_prompt=""):
        super().__init__(selector, query_engine_tools, llm, summarizer, verbose)
        self.set_sys_prompt(sys_prompt)

    def form_context(self):
        formatted_context = ""
        for entry in self.context:
            role = entry['role']
            message = entry['content']
            formatted_context += f"{role.capitalize()}: {message}\n"
        return formatted_context

    def get_completion_from_messages(self,message:str):
        self.__append_context(message,"user")
        #self.query(self.form_context())
        self.query(message)
    
    def __append_context(self,message:str, role:str):
        self.context.append({'role':role, 'content':f"{message}"})

    def set_sys_prompt(self,sys_prompt:str):
        self.sys_prompt = sys_prompt
        self.context.clear()
        self.__append_context(message=sys_prompt,role="system")