# 1
import markdown

markdown_string = '# Hello World'

# 2
html_string = markdown.markdown(markdown_string)
print(html_string)

# 3 
markdown_string = '''
# Hello World

This is a **great** tutorial about using Markdown in [Python](https://python.org).
'''

html_string = markdown.markdown(markdown_string)
print(html_string)