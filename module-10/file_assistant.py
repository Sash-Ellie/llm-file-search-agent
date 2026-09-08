"""
Task 1-2 Part 2: File Assistant Agent

Create an agent that can use the file tools to perform operations
based on natural language requests. This agent will interpret user
intent and use the appropriate tools.

Complete the TODOs below to implement the file assistant.
"""

import os
from dotenv import load_dotenv
import langroid as lr
import langroid.language_models as lm
from langroid.agent.tools.orchestration import DoneTool
from file_tools import ListDirTool, ReadFileTool, WriteFileTool

# Load environment variables from .env file
load_dotenv()

# Get model from environment, default to Gemini if not set
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gemini/gemini-2.5-flash")


class FileAssistantConfig(lr.ChatAgentConfig):
    """Configuration for the File Assistant agent."""
    
    # TODO 1: Set a descriptive name for the agent
    name: str = "FileAssistant"
    
    # TODO 2: Configure the LLM
    # Hint: Use lm.OpenAIGPTConfig with chat_model=CHAT_MODEL
    llm: lm.OpenAIGPTConfig = lm.OpenAIGPTConfig(
        chat_model=CHAT_MODEL,
        max_output_tokens=500,
        temperature=0.7,
    )

    system_message: str = """
    You are a helpful file assistant.
    You can list directories, read files, and write files using your tools.
    Use the correct tool based on the user's request.
    Return clear, user-friendly responses.
    """

    # TODO 3: Nudge the LLM to use tools when it forgets
    # IMPORTANT: This nudges the LLM to use a tool when it forgets
    handle_llm_no_tool:str  = f"""
        You FORGOT to use one of your TOOLs! Remember that:
        - {ListDirTool.name()}: list the contents of a directory
	- {ReadFileTool.name()}: read the contents of a file
	- {WriteFileTool.name()}: write content to a file
	- {DoneTool.name()}: finish the task and return the final response in the content 	   field
        """

    # TODO 4: Write a system message that:
    # - Explains the agent is a helpful file assistant
    # - Lists available tools (use tool.name() to get actual names):
    #   - ListDirTool for listing directory contents
    #   - ReadFileTool for reading files
    #   - WriteFileTool for writing files
    #   - DoneTool to signal completion and return results in `content` field
    # - Provides guidance on how to use tools appropriately
    # - Instructs to provide clear, helpful responses
    # - IMPORTANT: Must use DoneTool to return the summary
    # Regarding naming the tools, note that  the agent is unaware of the class names of
    # the tools, so you have to get the `name()` method of the tool class to
    # get the actual name, e.g. `ReadFileTool.name()`.
    # (Do not change the last two paragraphs of the system message!)
    system_message: str = f"""
    TODO: You are a helpful file assistant. Your job is to help users list directory 	contents, read files, and write files by using tools.

	Available tools:
	- {ListDirTool.name()}: use this to list files and folders in a directory.
	- {ReadFileTool.name()}: use this to read the contents of a file.
	- {WriteFileTool.name()}: use this to write content to a file.
	- {DoneTool.name()}: use this when the task is complete and put the final user-	    	   facing answer in the content field.

Choose the correct tool based on the user's request. Use one tool at a time, wait for the result, then decide what to do next. Always give clear, helpful responses.
    
    IMPORTANT: You CANNOT use multiple tools at once! Use one tool at a time,
        wait for the result, and THEN decide what to do next.
    
    When your task is complete, you MUST use the `{DoneTool.name()}` tool to 
    indicate completion, and use the `content` field to return any response you wish to 
    provide. It is CRITICAL to use the `content` field to return any results 
    sought by the user, since they will NOT be able to see anything outside of this tool!
    """


def run_file_assistant(prompt: str) -> str:
    """
    Create and run a file assistant agent with the given prompt.
    
    Args:
        prompt: The user's request to the file assistant
        
    Returns:
        str: The agent's response
    """
    # TODO 5: Create the agent configuration
    config = FileAssistantConfig()
    
    # TODO 6: Create the ChatAgent
    agent = lr.ChatAgent(config)
    
    # TODO 7: Enable the agent to use all file tools and the DoneTool
    agent.enable_message(ListDirTool)
    agent.enable_message(ReadFileTool)
    agent.enable_message(WriteFileTool)
    agent.enable_message(DoneTool)
    
    # TODO 8: Create a Task with the agent
    # Hint: Set interactive=False for automated operation
    task = lr.Task(agent, interactive=False)
    
    # TODO 9: Run the task with the prompt
    result = task.run(prompt)
    
    # TODO 10: Return the string representation of the result
    # Note: result is a ChatDocument, which has a content attribute of type str pass
    return result.content

# Example usage (uncomment to test)
# if __name__ == "__main__":
#     # Test listing files
#     response = run_file_assistant("List all files in the myfiles directory")
#     print("List response:")
#     print(response)
#     
#     # Test reading a file
#     response = run_file_assistant("Read the file myfiles/beethoven.md")
#     print("\nRead response:")
#     print(response)
#     
#     # Test writing a file
#     response = run_file_assistant("Write 'Hello, World!' to myfiles/test.txt")
#     print("\nWrite response:")
#     print(response)