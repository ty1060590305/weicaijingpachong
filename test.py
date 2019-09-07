import requests
from lxml import etree


def  wy163():
    url = 'http://quotes.money.163.com/trade/lsjysj_zhishu_000001.html?year=1992&season=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Cookie': 'P_INFO=piaoandaodao@163.com|1563184436|0|mail163|00&99|gud&1563114713&note_client#gud&null#10#0#0|&0|youdaodict_client&note_client|piaoandaodao@163.com; _ntes_nnid=7b94e6650045403a8aac88574734da77,1563184445438; _ntes_nuid=7b94e6650045403a8aac88574734da77; vinfo_n_f_l_n3=704fa4cd8fee2afb.1.3.1566632469878.1567264201875.1567472968502; vjuids=9ff9d05e1.16d0bce8b9b.0.13c95b3d98b4d; vjlast=1567861149.1567861149.30'}
    params = {
        'year': '1992',
        'season': '1'
    }
    page_text = requests.get(url=url, params=params, headers=headers).text
    tree = etree.HTML(page_text)
    title = tree.xpath('/html/head/title/text()')
    now=tree.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')

    print(title,'111')
    print(now)
    td_list = tree.xpath(
        '/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')
    print(td_list, type(td_list))
    #  /html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong
    # /html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[2]/strong[1]
    for td in td_list:
        szzs = td.xpath('./span/strong')
        print(szzs)
def sina():
    stock_id='sh000001'
    url = 'http://hq.sinajs.cn/list=s_{}'.format(stock_id)
    url='http://hq.sinajs.cn/list=s_sh000001'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    res=requests.get(url,headers)
    print(res.content)


if __name__ == '__main__':
    sina()