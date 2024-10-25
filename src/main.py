import os
import ast

def extract_docstrings(file_path):
    """Extracts docstrings from a Python file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        node = ast.parse(file.read(), filename=file_path)
        docstrings = {}
        
        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(item)
                if docstring:
                    docstrings[item.name] = docstring
        
    return docstrings

def generate_markdown(docstrings, file_name):
    """Generates Markdown documentation from extracted docstrings."""
    markdown_content = f"# Documentation for {file_name}\n\n"
    
    for name, doc in docstrings.items():
        markdown_content += f"## {name}\n\n{doc}\n\n"
    
    return markdown_content

def generate_documentation(directory):
    """Generates documentation for all Python files in the specified directory."""
    all_docstrings = {}
    
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            file_path = os.path.join(directory, filename)
            docstrings = extract_docstrings(file_path)
            all_docstrings[filename] = docstrings
    
    return all_docstrings

def save_markdown(markdown_content, output_file):
    """Saves the Markdown content to a file."""
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

def main():
    directory = input("Enter the directory containing Python files: ")
    output_file = input("Enter the output Markdown file name (e.g., documentation.md): ")
    
    all_docstrings = generate_documentation(directory)
    
    markdown_content = ""
    for file_name, docstrings in all_docstrings.items():
        markdown_content += generate_markdown(docstrings, file_name)
    
    save_markdown(markdown_content, output_file)
    print(f"Documentation generated and saved to {output_file}")

if __name__ == "__main__":
    main()
