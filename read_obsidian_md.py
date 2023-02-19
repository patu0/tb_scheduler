import markdown
from bs4 import BeautifulSoup

def num_extractor(string):
    # input: <time>-<element>
    # output: <time>
    time_list = [i for i in string if i.isdigit()]
    return int("".join(time_list))

def word_to_int(string):
    #hours
    split = string.split(' ')
    duration_str= split[0]
    extracted_num = num_extractor(duration_str)
    extracted_time_unit = time_unit_extractor(duration_str)
    return extracted_num
    #mins
    #none

# file_path = r"C:\Users\97pat\OneDrive\Documents\pat life\pages\Plans.md"
file_path = r"D:\Code\tb_scheduler\sample_2.md"


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
    print(row)
    print(word_to_int(row))
    

# interpret each row with content grab all items 
# 15-min
# 1-hour
# 1-hr

