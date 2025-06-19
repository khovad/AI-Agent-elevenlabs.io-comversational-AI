from elevenlabs.conversational_ai.conversation import ClientTools
from langchain.tools import DuckDuckGoSearchRun

def searchWeb(parameters):
    """Search the web using DuckDuckGo."""
    query = parameters.get("query")
    results = DuckDuckGoSearchRun(query=query)
    return results

def save_to_txt(parameters):
    """Save the provided text to a file."""
    filename = parameters.get("filename")
    data = parameters.get("data")

    formatted_data = f"{data}"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_data + "\n")

def create_html_file(parameters):
    """Create an HTML file with the provided content."""
    filename = parameters.get("filename")
    data = parameters.get("data")
    title = parameters.get("title")

    formated_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <p>{data}</div>
    </body>
    <html>
    """
    with open (filename, "w", encoding="utf-8") as file:
        file.write(formated_html)
    

client_tools = ClientTools()
client_tools.register("searchWeb", searchWeb)
client_tools.register("save_to_txt", save_to_txt)
client_tools.register("create_html_file", create_html_file)