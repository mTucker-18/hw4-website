import glob
import os
import markdown
from jinja2 import Template
import sys

# Initiate an empty list to push dicts into later

pages = []

def main():
    populate_dict()
    for page in pages:
        #page = markdown_conversion(page)
        final_page = replace_template(page)
        open(page['output_file'], "w+").write(final_page)

# Phase 1 - takes input from glob and os to make each dict within the pages list

def populate_dict():
    list_of_md = glob.glob("content/*.html")
    for page in list_of_md:
        file_html = os.path.basename(page)        
        name_only, extension = os.path.splitext(page)    
        pages.append({
            'title': 'Matthew Tucker',
            'file_name': str(page),
            'output_file': 'docs/' + str(file_html),
            'opening_text': 'Matthew Tucker',
            'sub_text': 'Coding Student',
            })

# Phase 2 - uses templating to replace chosen areas         

def replace_template(page):
    content_page = open(page['file_name']).read()
    base_html = open('templates/base.html').read()
    final_page = Template(base_html)
    final_page = final_page.render(
        title = page['title'],
        content = content_page,
        opening_text = page['opening_text'],
        sub_text = page['sub_text'],
        ) 
    return final_page  
     
# Phase 3 - supports markdown and converts markdown to html

def markdown_conversion(page):
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    data = open(page['file_name']).read()
    converted_html = md.convert(data)
    return converted_html

# Phase 4 - improved templating
    
# Phase 5 - manage.py generator 
    
def new_content():
    print("This is argv:", sys.argv)
    if sys.argv[3] == "build":
        print("Build was specified")
    elif sys.argv[3] == "new":
        print("New page was specified")
    else:
        print("Please specify ’build’ or ’new’")


main()
#if __name__ == "__main__":
#    main()

