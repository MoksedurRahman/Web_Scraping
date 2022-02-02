from bs4 import BeautifulSoup
markup = '''
<Html>
<Head><title>Example of Paragraph tag</title></Head>  
<Body>
<p> this is paragraph</p>
<!-- It is a Paragraph tag for creating the paragraph -->   
<p><b>HTML</b>stands for<i><u> Hyper Text Markup Language. </u> </i> It is used to create a web pages and applications. This language   
is easily understandable by the user and also be modifiable.<p>It is actually a Markup language, hence it provides a flexible way for designing the  
web pages along with the text.  </p><p>  
HTML file is made up of different elements. <b> An element </b> is a collection of <i> start tag, end tag, attributes and the text between them</i>.   
</p>  
</p>
<p> second paragraph</p>
<input name="email"/>
<div>
<div data-foo="value">foo!</div>
<b> 'b' tag use for bold text</b><i>important note formatted with italic tag</i><strong>strong also use to important note</strong>
<p>
set of link
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
<a href="https://cppsecrets.com"  class"python" id='link4'>InternShip</a>
</div>
</p> 
</Body>  
</Html>
'''
soup = BeautifulSoup(markup,'lxml')
link_sibling = soup.a
print(link_sibling.find_next_sibling('a'))
print(link_sibling.find_next_siblings('a'))