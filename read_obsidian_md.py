import markdown
from bs4 import BeautifulSoup



# file_path = r"C:\Users\97pat\OneDrive\Documents\pat life\pages\Plans.md"
file_path = r"D:\Code\tb_scheduler\sample_1.md"


f = open(file_path,'r')
# print("==f.read==")
# print(f.read())

htmlmarkdown = markdown.markdown(f.read())
# print("==html markdown==")
# print(htmlmarkdown)

soup = BeautifulSoup(htmlmarkdown, 'html.parser')

# print(soup.prettify())

# print(soup.get_text())
# print("".join(soup.strings))

split = "".join(soup.strings).split('\n')
split = split[1:-1] # remove empty start and end lines
for i, row in enumerate(split):
    
    print(i, row)

# interpret each row with content

def word_to_int():
    #hours
    #mins
    #none
