from crewai_tools import BaseTool
import os

class CodeCompilerTool(BaseTool):
    name: str = "Code Compiler Tool"
    description: str = "Compiles sections of code into structured files and directories based on enhanced semantic markers."

    def _run(self, code: str, project_name: str) -> str:
        desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')

        sections = {
            'agents.yaml': '',
            'tasks.yaml': '',
            'crew.py': '',
            'main.py': '',
            'pyproject.toml': ''
        }

        # Define a list of known section keys with enhanced delimiters
        section_keys = ['##== agents.yaml ==##', '##== tasks.yaml ==##', '##== crew.py ==##', '##== main.py ==##', '##== pyproject.toml ==##']
        
        # Split the code using a newline and initialize variables
        lines = code.split('\n')
        current_section = None
        
        # Iterate through each line to determine and collect sections
        for line in lines:
            # Check if the line contains a section key
            if any(key in line for key in section_keys):
                # Extract the key name by removing delimiters
                current_section = line.strip('##== ').strip(' ==##')
            elif current_section:
                # Append the line to the correct section
                sections[current_section] += line + '\n'

        project_dir = os.path.join(desktop_path, project_name)
        src_dir = os.path.join(project_dir, 'src', project_name)
        config_dir = os.path.join(src_dir, 'config')
        tools_dir = os.path.join(src_dir, 'tools')

        os.makedirs(config_dir, exist_ok=True)
        os.makedirs(tools_dir, exist_ok=True)

        with open(os.path.join(config_dir, 'agents.yaml'), 'w') as f:
            f.write(sections['agents.yaml'])
        with open(os.path.join(config_dir, 'tasks.yaml'), 'w') as f:
            f.write(sections['tasks.yaml'])
        with open(os.path.join(src_dir, 'crew.py'), 'w') as f:
            f.write(sections['crew.py'])
        with open(os.path.join(src_dir, 'main.py'), 'w') as f:
            f.write(sections['main.py'])
        with open(os.path.join(project_dir, 'pyproject.toml'), 'w') as f:
            f.write(sections['pyproject.toml'])

        open(os.path.join(src_dir, '__init__.py'), 'w').close()
        open(os.path.join(tools_dir, '__init__.py'), 'w').close()
        open(os.path.join(project_dir, '.env'), 'w').close()

        return f"Project '{project_name}' compiled successfully at {project_dir}"

# Usage example
# tool = CodeCompilerTool()
# result = tool.run(code=loaded_code, project_name='nome_do_projeto')
# print(result)

