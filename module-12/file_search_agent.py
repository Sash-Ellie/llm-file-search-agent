"""
Task 3-4: File Search Agent

Create a specialized agent that can search through files to find content
matching a user's query. The agent should use file tools to explore
directories and examine file contents.

Complete the TODOs below to implement the file search agent.
"""

import os
from dotenv import load_dotenv
import langroid as lr
import langroid.language_models as lm
from langroid.agent.tools.orchestration import DoneTool
from file_tools import ListDirTool, ReadFileTool

# Load environment variables from .env file
load_dotenv()

# Get model from environment, default to Gemini if not set
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gemini/gemini-2.0-flash-exp")


class FileSearchAgentConfig(lr.ChatAgentConfig):
    """Configuration for the file search specialist agent."""
    
    # TODO 1: Set a descriptive name for the agent
    name: str = "FileSearchAgent"
    
    # TODO 2: Configure the LLM
    # Hint: Use lm.OpenAIGPTConfig with chat_model=CHAT_MODEL
    llm: lm.OpenAIGPTConfig = lm.OpenAIGPTConfig(
        chat_model = CHAT_MODEL,
        max_output_tokens = 500,
        temperature = 0.0)


    # IMPORTANT -- this nudges the agent to use tools when it forgets
    handle_llm_no_tool:str = f"""
    You FORGOT to use one of your TOOLS! Remember:
    - {ListDirTool.name()}: list files in the search directory.
    - {ReadFileTool.name()}: read file contents using the full file path.
    - {DoneTool.name()}: finish the task and return the final answer in the content field.
    """

    # TODO 3: Write a system message that:
    # - Explains the agent is a file search specialist
    # - Describes the search process:
    #   1. Use ListDirTool to list files
    #   2. Use ReadFileTool to examine contents
    #   3. Check if content matches the query
    #   4. Track all matching files
    # - Explains what makes a file match (keywords, topics, relevance)
    # - IMPORTANT: (a) Must use DoneTool to return results, with content field
    #   containing the string response.
    # - IMPORTANT: (b) If no matches, the content field must be EMPTY!
    # Note when naming tools in the system message, keep in mind that the
    # LLM does not know about the Tool Class names like ListDirTool, etc.
    # Instead, it is aware of the `request` value in the Tool's definition,
    # which is the name used in the system message. You should access this
    # value using the Tool's static method name(), e.g. ListDirTool.name(),
    # so you must use that in the system message when mentioning a tool.

    system_message: str = f"""
    You are a specialized file search agent.

    Your job is to search through files in a directory and find files that match the user's query.

    Search process:
    1. Use {ListDirTool.name()} to list the files in the directory.
    2. For each relevant file, use {ReadFileTool.name()} with the full file path.
    3. Compare the file contents to the user's query.
    4. A file matches if it contains relevant keywords, related topics, or clearly useful content.
    5. Keep track of all matching files.

    When you find matches, return the file names with brief explanations of why each file is relevant.

    IMPORTANT: You must use {DoneTool.name()} when the task is complete.
    Put the final user-facing response in the `content` field.

    IMPORTANT: If no files match the query, the `content` field must be EMPTY.
    """


def run_file_search(directory: str, query: str) -> str:
    """
    Create and run a file search agent to find files matching a query.
    
    Args:
        directory: The directory to search in
        query: The search query to match against file contents
        
    Returns:
        A string listing the matching files, or a message if no matches
    """
    # TODO 4: Create the FileSearchAgentConfig
    config = FileSearchAgentConfig()
    
    # TODO 5: Create the ChatAgent
    agent = lr.ChatAgent(config)
    
    # TODO 6: Enable agent to use the required tools
    
    agent.enable_message(ListDirTool)
    agent.enable_message(ReadFileTool)
    agent.enable_message(DoneTool)

    # TODO 7: Create a Task with interactive=False
    task = lr.Task(agent, interactive = False)
    
    # TODO 8: Create a prompt for the agent
    # Different from system message (which is a generic instruction),
    # this prompt should be specific to the current search task of
    # searching in a directory with a query.
    prompt = f"""
    Search the directory `{directory}` for files matching this query:

    `{query}`

    Use {ListDirTool.name()} first to list the directory.
    Then use {ReadFileTool.name()} to read relevant files using their full paths.
    Return matching file names with brief explanations.

    If no files match, return an empty content field using {DoneTool.name()}.
    """
    
    # TODO 9: Run the task and get the result
    result = task.run(prompt)
    
    # TODO 10: Return the result content
    # Hint: Result is of type ChatDocument, which has a content field of type str
    pass  # Replace with return statement

    return result.content


# TODO 11: Create and export the agent for use by other modules
# This allows the search tool to import and use this agent
# Steps:
# 1. Create a FileSearchAgentConfig instance
# 2. Create a ChatAgent with that config
# 3. Enable the required tools on the agent
# (can be done in 2 lines of code)
file_search_agent = lr.ChatAgent(FileSearchAgentConfig())
file_search_agent.enable_message(ListDirTool)
file_search_agent.enable_message(ReadFileTool)
file_search_agent.enable_message(DoneTool)