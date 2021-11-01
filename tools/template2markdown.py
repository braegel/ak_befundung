import sys
import re

tag_doctype=re.compile("<!DOCTYPE.*?>")
tag_html=re.compile("<html>[\n\r\s]*(.*?)[\n\r\s]*</html>", re.DOTALL)
tag_head=re.compile("<head>[\n\r\s]*(.*?)[\n\r\s]*[\n\r\s]*</head>", re.DOTALL)
tag_title=re.compile("<title>[\n\r\s]*(.*?)[\n\r\s]*</title>", re.DOTALL)
tag_empty=re.compile("<.*? />")
tag_comment=re.compile("<!--.*?-->", re.DOTALL)
tag_meta=re.compile("<meta.*?>")
tag_script=re.compile("<script.*?>.*?</script>", re.DOTALL)
tag_link=re.compile("<link.*?>")
tag_body=re.compile("<body>[\n\r\s]*(.*?)[\n\r\s]*</body>", re.DOTALL)
tag_section=re.compile("<section.*?>[\n\r\s]*(.*?)[\n\r\s]*</section>", re.DOTALL)
tag_header_1=re.compile("<header class=\"level1\".*?>[\n\r\s]*(.*?)[\n\r\s]*</header>", re.DOTALL)
tag_p=re.compile("<p.*?>[\n\r\s]*(.*?)[\n\r\s]*</p>", re.DOTALL)
tag_textarea=re.compile("<textarea.*?>[\n\r\s]*(.*?)[\n\r\s]*</textarea>", re.DOTALL)
tag_table=re.compile("[\n\r\s]*<table>[\n\r\s]*(.*?)[\n\r\s]*</table>[\n\r\s]*", re.DOTALL)
tag_th=re.compile("<th>[\n\r\s]*(.*?)[\n\r\s]*</th>", re.DOTALL)
tag_td=re.compile("<td>[\n\r\s]*(.*?)[\n\r\s]*</td>", re.DOTALL)
tag_tr=re.compile("<tr.*?>[\n\r\s]*(.*?)[\n\r\s]*</tr>", re.DOTALL)
tag_label=re.compile("<label.*?>[\n\r\s]*(.*?)[\n\r\s]*</label>[\n\r\s]*")
tag_select=re.compile("<select.*?>[\n\r\s]*(.*?)[\n\r\s]*</select>", re.DOTALL)
tag_option=re.compile("<option.*?>[\n\r\s]*(.*?)[\n\r\s]*</option>")
mybreak=re.compile("BREAK")

def html2md(md):
    md=tag_doctype.sub('',md)
    md=tag_html.sub(r'\1',md)
    md=tag_head.sub(r'\1',md)
    md=tag_title.sub(r'# \1',md)
    md=tag_empty.sub('',md)
    md=tag_comment.sub('',md)
    md=tag_meta.sub('',md)
    md=tag_script.sub('',md)
    md=tag_link.sub('',md)
    md=tag_body.sub(r'\1',md)
    md=tag_section.sub(r'\1',md)
    md=tag_header_1.sub(r'BREAK## \1',md)    
    md=tag_p.sub(r'\1',md)
    md=tag_textarea.sub(r'\1',md)
    md=tag_table.sub(r'\1',md)
    md=tag_th.sub(r'BREAK- \1',md)
    md=tag_td.sub(r'',md)
    md=tag_tr.sub(r'\1',md)
    md=tag_label.sub(r'\1',md)
    md=tag_select.sub(r'\1',md)
    md=tag_option.sub(r'',md)
    md=tag_table.sub(r'\1',md) #subtable
    md=mybreak.sub('\n',md)
    return md

template_path=str(sys.argv[1])

f = open(template_path, "r")
html=f.read()

md=html2md(html)

lines = md.split("\n")
non_empty_lines = [line for line in lines if line.strip() != ""]
md = ""
for line in non_empty_lines:
    md += line + "\n"
print(md)    
