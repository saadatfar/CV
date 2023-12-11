import re

def latex_to_markdown(latex_content):
    # Replace LaTeX commands with Markdown equivalents

    # Remove links
    latex_content = re.sub(r'\\link\{(.+?)\}\{(.+?)\}', r'', latex_content)
    latex_content = re.sub(r'\\titledesc\{(.+?)\}', r'- \1', latex_content)
    latex_content = re.sub(r'\\begin\{.*?}', r'', latex_content)
    latex_content = re.sub(r'\\end\{.*?}', r'', latex_content)
    latex_content = re.sub(r'\\medskip', r'', latex_content)
    latex_content = re.sub(r'\\justifying', r'', latex_content)
    latex_content = re.sub(r'\\noindent', r'', latex_content)
    latex_content = re.sub(r'\\divider', r'', latex_content)
    latex_content = re.sub(r'\\par', r'', latex_content)
    latex_content = re.sub(r'\\smallskip', r'', latex_content)

    # Convert special chars and texts
    latex_content = re.sub(r'\$\\sim\$', r'~', latex_content)
    latex_content = re.sub(r'\\\&', r'&', latex_content)
    latex_content = re.sub(r'\\\#', r'#', latex_content)
    latex_content = re.sub(r'\\Latex', r'Latex', latex_content)


    latex_content = re.sub(r'\\usepackage\{.*?}', r'', latex_content)
    

    # Remove comments and tabs
    latex_content = re.sub(r'\%.*', r'', latex_content)
    latex_content = re.sub(r'\t', r'', latex_content)

    # Convert items
    latex_content = re.sub(r'\\item', r'-', latex_content)

    # Convert Heading
    latex_content = re.sub(r'\\name[\s\S]*?\{(.+?)\}', r'# \1', latex_content)
    latex_content = re.sub(r'\\tagline[\s\S]*?\{(.+?)\}', r'## \1', latex_content)
    latex_content = re.sub(r'\\email[\s\S]*?\{(.+?)\}', r'Email: \1', latex_content)
    latex_content = re.sub(r'\\homepage[\s\S]*?\{(.+?)\}', r'Homepage: \1', latex_content)
    latex_content = re.sub(r'\\linkedin[\s\S]*?\{(.+?)\}', r'Linkedin: \1', latex_content)
    latex_content = re.sub(r'\\location[\s\S]*?\{(.+?)\}', r'Location: \1', latex_content)
    latex_content = re.sub(r'\\phone[\s\S]*?\{(.+?)\}', r'Phone: \1', latex_content)
    latex_content = re.sub(r'\\personalinfo[\s\S]*?\{([\s\S]*?)\}', r'\1', latex_content)

    # Convert sections
    latex_content = re.sub(r'\\cvsection[\s\S]*?\{(.+?)\}', r'# \1', latex_content)
    latex_content = re.sub(r'\\cvevent[\s\S]*?\{(.*?)\}[\s\S]*?\{(.*?)\}[\s\S]*?\{(.*?)\}[\s\S]*?\{(.*?)\}',
                           r'## \1 - \2 - \3\n - \4', latex_content)
    latex_content = re.sub(r'\\cvproject[\s\S]*?\{(.*?)\}[\s\S]*?\{(.*?)\}[\s\S]*?\{(.*?)\}',
                           r'## \1 - \3\n', latex_content)
    latex_content = re.sub(r'\\cvskill[\s\S]*?\{(.*?)\}[\s\S]*?\{([\s\S]*?)\}', r'## \1\n\2', latex_content)
    
    #Remove Boxes
    latex_content = re.sub(r'\\vbox[\s\S]*?\{([\s\S]*?)\}', r'\1\n', latex_content)


    # Cleanup
    latex_content = re.sub(r'\\.*', r'', latex_content)
    latex_content = re.sub(r'\-\-', r'-', latex_content)
    latex_content = re.sub(r'[ ]*\n', r'\n', latex_content)
    latex_content = re.sub(r'[\-]*\n', r'\n', latex_content)
    latex_content = re.sub(r'\n[ ]*', r'\n', latex_content)
    latex_content = re.sub(r'\n\n+', r'\n', latex_content)
    latex_content = re.sub(r'#+\n', r'', latex_content)

    #Reformat new lines
    latex_content = re.sub(r'\n\#([^#\n]+)',
                           r'\n\n<!-------------------  \1  ---------------------------->\n#\1', latex_content)
    latex_content = re.sub(r'\n(\#\#[^#])', r'\n\n\1', latex_content)

    return latex_content

def convert_file(latex_file_path, markdown_file_path):
    with open(latex_file_path, 'r', encoding='utf-8') as file:
        latex_content = file.read()

    markdown_content = latex_to_markdown(latex_content)

    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

    print(f"Converted {latex_file_path} to {markdown_file_path}")

# Example usage
convert_file('CV.tex', 'CV.md')
