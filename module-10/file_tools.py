"""
Task 1-2 Part 1: Basic File Tools

Implement the handle() method for each tool class to perform
file operations. These tools will be used by agents to interact
with the file system.
"""

import os
from langroid.pydantic_v1 import Field
import langroid as lr


class ListDirTool(lr.ToolMessage):
    """Tool to list files and directories in a given path."""
    
    request: str = "list_dir"
    #TODO 1: Add a clear purpose description
    purpose: str = "List the contents of a directory"

    # TODO 2: Add a path field with description
    path: str = Field(
        ...,
        description="Path to the directory"
    )
    
    def handle(self) -> str:
        """
        List directory contents.
        
        TODO 3: Implement this method to:
        1. Check if the path exists and is a directory
        2. If valid, return a sorted, newline-separated list of directory contents
        3. If invalid, return an appropriate error message, saying "Error:..."
        
        Returns:
            str: Directory contents or error message
        """   
        try:
            files = sorted(os.listdir(self.path))
            return "\n".join(files)
        except FileNotFoundError:
            return f"Error:Directory not found: {self.path}"
        except NotADirectoryError:
            return f"Eroor: Not a directory: {self.path}"
        except Exception as e:
            return f"Error listing directory: {e}"


class ReadFileTool(lr.ToolMessage):
    """Tool to read file contents."""
    
    request: str = "read_file"
    # TODO 4: Add a clear purpose description
    purpose: str = "Read the contents of a file"

    # TODO 5: Add a path field with description
    path: str = Field(
        ...,
        description="Path to the file"
    )
    
    def handle(self) -> str:
        """
        Read file contents.
        
        TODO 6: Implement this method to:
        1. Attempt to read the file at the given path
        2. Return the complete file contents as a string
        3. Handle errors gracefully (file not found, permissions, etc.) -
            if error, return a message starting with "Error: ..."
        
        Returns:
            str: File contents or error message
        """
    
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return f"File not found: {self.path}"
        except Exception as e:
            return f"Error reading file: {e}"


class WriteFileTool(lr.ToolMessage):
    """Tool to write content to a file."""
    
    request: str = "write_file"

    # TODO 7: Add a clear purpose description
    purpose: str = "Write content to a file"

    # TODO 8: Add path and content fields with descriptions
    path: str = Field(..., description="Path to the file or directory")
    content: str = Field(..., description="Content to write to the file")
    
    def handle(self) -> str:
        """
        Write content to file.
        
        TODO 9: Implement this method to:
        1. Write the provided content to the specified file path
        2. Create the file if it doesn't exist (overwrite if it does)
        3. Return a success message indicating the file path, and confirming the write
            (use language "Successfully wrote ...")
        4. Handle errors gracefully (permissions, invalid path, etc.)
           If error, return a message starting with "Error: ..."
        
        Returns:
            str: Success message or error message
        """
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                f.write(self.content)
            return f"Successfully wrote to {self.path}"
        except Exception as e:
            return f"Error writing file: {e}"
