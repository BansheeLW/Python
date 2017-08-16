import  requests
from  bs4 import  BeautifulSoup
import xlwt



# 设置Excel样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


#打开excel文件
data=xlwt.Workbook()
#获取其中的一个sheet
table=data.add_sheet('tokyo')

response = requests.get("http://www.szsti.gov.cn/services/hightech/default.aspx")
soup = BeautifulSoup(response.text,"html.parser")
target = soup.find(id="data_list_container").findAll("tr")
row=0
col=0
tr = target[0]
ths = tr.findAll("th")  # 获取所有的 td
th = [x for x in ths]
index = th[0].text.strip()
serialNo = th[1].text.strip()
companyName = th[2].text.strip()
location = th[3].text.strip()
domain = th[4].text.strip()
category = th[5].text.strip()
table.write(row,col,index,set_style('Arial', 220))
table.write(row,col+1,serialNo,set_style('Arial', 220))
table.write(row,col+2,companyName,set_style('Arial', 220))
table.write(row, col + 3, location,set_style('Arial', 220))
table.write(row, col + 4, domain,set_style('Arial', 220))
table.write(row, col + 5, category,set_style('Arial', 220))
data.save('TokyoHot.xls')


