import requests
from time_handeling import TimeHandling
# data = {'Meta Data': {'1. Information': 'Daily Prices (open, high, low, close) and Volumes', '2. Symbol': 'TSLA', '3. Last Refreshed': '2024-08-23', '4. Output Size': 'Compact', '5. Time Zone': 'US/Eastern'}, 'Time Series (Daily)': {'2024-08-23': {'1. open': '214.4550', '2. high': '221.4800', '3. low': '214.2100', '4. close': '220.3200', '5. volume': '81525207'}, '2024-08-22': {'1. open': '223.8200', '2. high': '224.8000', '3. low': '210.3200', '4. close': '210.6600', '5. volume': '79514482'}, '2024-08-21': {'1. open': '222.6700', '2. high': '224.6594', '3. low': '218.8600', '4. close': '223.2700', '5. volume': '70145964'}, '2024-08-20': {'1. open': '224.8800', '2. high': '228.2200', '3. low': '219.5600', '4. close': '221.1000', '5. volume': '74001182'}, '2024-08-19': {'1. open': '217.0700', '2. high': '222.9800', '3. low': '214.0900', '4. close': '222.7200', '5. volume': '76435222'}, '2024-08-16': {'1. open': '211.1500', '2. high': '219.8000', '3. low': '210.8000', '4. close': '216.1200', '5. volume': '88765122'}, '2024-08-15': {'1. open': '205.0200', '2. high': '215.8800', '3. low': '204.8200', '4. close': '214.1400', '5. volume': '89848530'}, '2024-08-14': {'1. open': '207.3900', '2. high': '208.4400', '3. low': '198.7500', '4. close': '201.3800', '5. volume': '70250014'}, '2024-08-13': {'1. open': '198.4700', '2. high': '208.4900', '3. low': '197.0600', '4. close': '207.8300', '5. volume': '76247387'}, '2024-08-12': {'1. open': '199.0200', '2. high': '199.2600', '3. low': '194.6700', '4. close': '197.4900', '5. volume': '64044903'}, '2024-08-09': {'1. open': '197.0500', '2. high': '200.8800', '3. low': '195.1100', '4. close': '200.0000', '5. volume': '58648274'}, '2024-08-08': {'1. open': '195.7000', '2. high': '200.7000', '3. low': '192.0400', '4. close': '198.8400', '5. volume': '65033874'}, '2024-08-07': {'1. open': '200.7700', '2. high': '203.4900', '3. low': '191.4800', '4. close': '191.7600', '5. volume': '71159778'}, '2024-08-06': {'1. open': '200.7500', '2. high': '202.9000', '3. low': '192.6700', '4. close': '200.6400', '5. volume': '73783942'}, '2024-08-05': {'1. open': '185.2200', '2. high': '203.8799', '3. low': '182.0000', '4. close': '198.8800', '5. volume': '100308836'}, '2024-08-02': {'1. open': '214.8800', '2. high': '216.1300', '3. low': '205.7800', '4. close': '207.6700', '5. volume': '82880120'}, '2024-08-01': {'1. open': '227.6900', '2. high': '231.8670', '3. low': '214.3328', '4. close': '216.8600', '5. volume': '83861898'}, '2024-07-31': {'1. open': '227.9000', '2. high': '234.6800', '3. low': '226.7875', '4. close': '232.0700', '5. volume': '67497011'}, '2024-07-30': {'1. open': '232.2500', '2. high': '232.4100', '3. low': '220.0000', '4. close': '222.6200', '5. volume': '100560334'}, '2024-07-29': {'1. open': '224.9000', '2. high': '234.2700', '3. low': '224.7000', '4. close': '232.1000', '5. volume': '129201789'}, '2024-07-26': {'1. open': '221.1900', '2. high': '222.2799', '3. low': '215.3300', '4. close': '219.8000', '5. volume': '94604145'}, '2024-07-25': {'1. open': '216.8000', '2. high': '226.0000', '3. low': '216.2310', '4. close': '220.2500', '5. volume': '100636466'}, '2024-07-24': {'1. open': '225.4200', '2. high': '225.9900', '3. low': '214.7100', '4. close': '215.9900', '5. volume': '167942939'}, '2024-07-23': {'1. open': '253.6000', '2. high': '255.7594', '3. low': '245.6300', '4. close': '246.3800', '5. volume': '111928192'}, '2024-07-22': {'1. open': '244.2100', '2. high': '253.2100', '3. low': '243.7500', '4. close': '251.5100', '5. volume': '101225430'}, '2024-07-19': {'1. open': '247.7900', '2. high': '249.4400', '3. low': '236.8300', '4. close': '239.2000', '5. volume': '87403903'}, '2024-07-18': {'1. open': '251.0900', '2. high': '257.1400', '3. low': '247.2000', '4. close': '249.2300', '5. volume': '110869037'}, '2024-07-17': {'1. open': '252.7300', '2. high': '258.4700', '3. low': '246.1820', '4. close': '248.5000', '5. volume': '115584810'}, '2024-07-16': {'1. open': '255.3100', '2. high': '258.6200', '3. low': '245.8001', '4. close': '256.5600', '5. volume': '126332470'}, '2024-07-15': {'1. open': '255.9700', '2. high': '265.6000', '3. low': '251.7300', '4. close': '252.6400', '5. volume': '146912920'}, '2024-07-12': {'1. open': '235.8000', '2. high': '251.8400', '3. low': '233.0912', '4. close': '248.2300', '5. volume': '155955773'}, '2024-07-11': {'1. open': '263.3000', '2. high': '271.0000', '3. low': '239.6500', '4. close': '241.0300', '5. volume': '221707273'}, '2024-07-10': {'1. open': '262.8000', '2. high': '267.5900', '3. low': '257.8600', '4. close': '263.2600', '5. volume': '128519430'}, '2024-07-09': {'1. open': '251.0000', '2. high': '265.6100', '3. low': '250.3000', '4. close': '262.3300', '5. volume': '160742516'}, '2024-07-08': {'1. open': '247.7100', '2. high': '259.4390', '3. low': '244.5700', '4. close': '252.9400', '5. volume': '157219580'}, '2024-07-05': {'1. open': '249.8100', '2. high': '252.3700', '3. low': '242.4601', '4. close': '251.5200', '5. volume': '154501152'}, '2024-07-03': {'1. open': '234.5600', '2. high': '248.3500', '3. low': '234.2500', '4. close': '246.3900', '5. volume': '166561471'}, '2024-07-02': {'1. open': '218.8900', '2. high': '231.3000', '3. low': '218.0600', '4. close': '231.2600', '5. volume': '205047920'}, '2024-07-01': {'1. open': '201.0200', '2. high': '213.2300', '3. low': '200.8500', '4. close': '209.8600', '5. volume': '135691395'}, '2024-06-28': {'1. open': '199.5500', '2. high': '203.2000', '3. low': '195.2600', '4. close': '197.8800', '5. volume': '95438068'}, '2024-06-27': {'1. open': '195.1700', '2. high': '198.7200', '3. low': '194.0500', '4. close': '197.4200', '5. volume': '72746521'}, '2024-06-26': {'1. open': '186.5400', '2. high': '197.7550', '3. low': '186.3600', '4. close': '196.3700', '5. volume': '95737066'}, '2024-06-25': {'1. open': '184.4000', '2. high': '187.9700', '3. low': '182.0100', '4. close': '187.3500', '5. volume': '63678265'}, '2024-06-24': {'1. open': '184.9700', '2. high': '188.8000', '3. low': '182.5500', '4. close': '182.5800', '5. volume': '61992070'}, '2024-06-21': {'1. open': '182.3000', '2. high': '183.9500', '3. low': '180.6900', '4. close': '183.0100', '5. volume': '63029482'}, '2024-06-20': {'1. open': '184.6800', '2. high': '185.2100', '3. low': '179.6600', '4. close': '181.5700', '5. volume': '55893139'}, '2024-06-18': {'1. open': '186.5600', '2. high': '187.2000', '3. low': '182.3700', '4. close': '184.8600', '5. volume': '68982265'}, '2024-06-17': {'1. open': '177.9200', '2. high': '188.8100', '3. low': '177.0000', '4. close': '187.4400', '5. volume': '109786083'}, '2024-06-14': {'1. open': '185.8000', '2. high': '186.0000', '3. low': '176.9200', '4. close': '178.0100', '5. volume': '82038194'}, '2024-06-13': {'1. open': '188.3900', '2. high': '191.0800', '3. low': '181.2300', '4. close': '182.4700', '5. volume': '118984122'}, '2024-06-12': {'1. open': '171.1200', '2. high': '180.5500', '3. low': '169.8000', '4. close': '177.2900', '5. volume': '90389446'}, '2024-06-11': {'1. open': '173.9200', '2. high': '174.7500', '3. low': '167.4100', '4. close': '170.6600', '5. volume': '64761928'}, '2024-06-10': {'1. open': '176.0600', '2. high': '178.5700', '3. low': '173.1700', '4. close': '173.7900', '5. volume': '50869682'}, '2024-06-07': {'1. open': '176.1300', '2. high': '179.3500', '3. low': '175.5800', '4. close': '177.4800', '5. volume': '56244932'}, '2024-06-06': {'1. open': '174.6000', '2. high': '179.7300', '3. low': '172.7300', '4. close': '177.9400', '5. volume': '69887024'}, '2024-06-05': {'1. open': '175.3500', '2. high': '176.1500', '3. low': '172.1300', '4. close': '175.0000', '5. volume': '57953756'}, '2024-06-04': {'1. open': '174.7750', '2. high': '177.7550', '3. low': '174.0000', '4. close': '174.7700', '5. volume': '60056340'}, '2024-06-03': {'1. open': '178.1300', '2. high': '182.6389', '3. low': '174.4900', '4. close': '176.2900', '5. volume': '68568920'}, '2024-05-31': {'1. open': '178.5000', '2. high': '180.3200', '3. low': '173.8200', '4. close': '178.0800', '5. volume': '67314602'}, '2024-05-30': {'1. open': '178.5750', '2. high': '182.6700', '3. low': '175.3800', '4. close': '178.7900', '5. volume': '77784755'}, '2024-05-29': {'1. open': '174.1900', '2. high': '178.1500', '3. low': '173.9300', '4. close': '176.1900', '5. volume': '54782649'}, '2024-05-28': {'1. open': '176.4000', '2. high': '178.2500', '3. low': '173.1600', '4. close': '176.7500', '5. volume': '59736620'}, '2024-05-24': {'1. open': '174.8350', '2. high': '180.0800', '3. low': '173.7300', '4. close': '179.2400', '5. volume': '65584478'}, '2024-05-23': {'1. open': '181.8000', '2. high': '181.9000', '3. low': '173.2600', '4. close': '173.7400', '5. volume': '71975496'}, '2024-05-22': {'1. open': '182.8500', '2. high': '183.8000', '3. low': '178.1200', '4. close': '180.1100', '5. volume': '88313477'}, '2024-05-21': {'1. open': '175.5100', '2. high': '186.8750', '3. low': '174.7100', '4. close': '186.6000', '5. volume': '115266512'}, '2024-05-20': {'1. open': '177.5600', '2. high': '177.7540', '3. low': '173.5200', '4. close': '174.9500', '5. volume': '61727425'}, '2024-05-17': {'1. open': '173.5500', '2. high': '179.6300', '3. low': '172.7500', '4. close': '177.4600', '5. volume': '77445845'}, '2024-05-16': {'1. open': '174.1000', '2. high': '175.7900', '3. low': '171.4300', '4. close': '174.8400', '5. volume': '59812220'}, '2024-05-15': {'1. open': '179.9000', '2. high': '180.0000', '3. low': '173.1100', '4. close': '173.9900', '5. volume': '79662993'}, '2024-05-14': {'1. open': '174.4959', '2. high': '179.4900', '3. low': '174.0700', '4. close': '177.5500', '5. volume': '86407422'}, '2024-05-13': {'1. open': '170.0000', '2. high': '175.4000', '3. low': '169.0000', '4. close': '171.8900', '5. volume': '67018903'}, '2024-05-10': {'1. open': '173.0500', '2. high': '173.0599', '3. low': '167.7500', '4. close': '168.4700', '5. volume': '72627178'}, '2024-05-09': {'1. open': '175.0100', '2. high': '175.6200', '3. low': '171.3700', '4. close': '171.9700', '5. volume': '65950292'}, '2024-05-08': {'1. open': '171.5900', '2. high': '176.0600', '3. low': '170.1500', '4. close': '174.7200', '5. volume': '79969488'}, '2024-05-07': {'1. open': '182.4000', '2. high': '183.2600', '3. low': '177.4000', '4. close': '177.8100', '5. volume': '75045854'}, '2024-05-06': {'1. open': '183.8000', '2. high': '187.5600', '3. low': '182.2000', '4. close': '184.7600', '5. volume': '84390253'}, '2024-05-03': {'1. open': '182.1000', '2. high': '184.7800', '3. low': '178.4200', '4. close': '181.1900', '5. volume': '75491539'}, '2024-05-02': {'1. open': '182.8600', '2. high': '184.6000', '3. low': '176.0200', '4. close': '180.0100', '5. volume': '89148041'}, '2024-05-01': {'1. open': '182.0000', '2. high': '185.8600', '3. low': '179.0100', '4. close': '179.9900', '5. volume': '92829719'}, '2024-04-30': {'1. open': '186.9800', '2. high': '190.9500', '3. low': '182.8401', '4. close': '183.2800', '5. volume': '127031787'}, '2024-04-29': {'1. open': '188.4200', '2. high': '198.8700', '3. low': '184.5400', '4. close': '194.0500', '5. volume': '243869678'}, '2024-04-26': {'1. open': '168.8500', '2. high': '172.1200', '3. low': '166.3700', '4. close': '168.2900', '5. volume': '109815725'}, '2024-04-25': {'1. open': '158.9600', '2. high': '170.8800', '3. low': '158.3600', '4. close': '170.1800', '5. volume': '126427521'}, '2024-04-24': {'1. open': '162.8400', '2. high': '167.9700', '3. low': '157.5100', '4. close': '162.1300', '5. volume': '181178020'}, '2024-04-23': {'1. open': '143.3300', '2. high': '147.2600', '3. low': '141.1100', '4. close': '144.6800', '5. volume': '124545104'}, '2024-04-22': {'1. open': '140.5600', '2. high': '144.4400', '3. low': '138.8025', '4. close': '142.0500', '5. volume': '107097564'}, '2024-04-19': {'1. open': '148.9700', '2. high': '150.9400', '3. low': '146.2200', '4. close': '147.0500', '5. volume': '87074500'}, '2024-04-18': {'1. open': '151.2500', '2. high': '152.2000', '3. low': '148.7000', '4. close': '149.9300', '5. volume': '96098830'}, '2024-04-17': {'1. open': '157.6400', '2. high': '158.3300', '3. low': '153.7800', '4. close': '155.4500', '5. volume': '82439718'}, '2024-04-16': {'1. open': '156.7420', '2. high': '158.1900', '3. low': '153.7500', '4. close': '157.1100', '5. volume': '96999956'}, '2024-04-15': {'1. open': '170.2400', '2. high': '170.6900', '3. low': '161.3800', '4. close': '161.4800', '5. volume': '100245310'}, '2024-04-12': {'1. open': '172.3400', '2. high': '173.8099', '3. low': '170.3644', '4. close': '171.0500', '5. volume': '64722669'}, '2024-04-11': {'1. open': '172.5500', '2. high': '175.8800', '3. low': '168.5100', '4. close': '174.6000', '5. volume': '94515987'}, '2024-04-10': {'1. open': '173.0400', '2. high': '174.9300', '3. low': '170.0100', '4. close': '171.7600', '5. volume': '84532407'}, '2024-04-09': {'1. open': '172.9100', '2. high': '179.2200', '3. low': '171.9200', '4. close': '176.8800', '5. volume': '102327658'}, '2024-04-08': {'1. open': '169.3400', '2. high': '174.5000', '3. low': '167.7900', '4. close': '172.9800', '5. volume': '104039371'}, '2024-04-05': {'1. open': '169.0800', '2. high': '170.8600', '3. low': '160.5100', '4. close': '164.9000', '5. volume': '136439809'}, '2024-04-04': {'1. open': '170.0700', '2. high': '177.1900', '3. low': '168.0100', '4. close': '171.1100', '5. volume': '122061224'}, '2024-04-03': {'1. open': '164.0200', '2. high': '168.8200', '3. low': '163.2800', '4. close': '168.3800', '5. volume': '82223543'}}}

# Function to get the closing time for a specific date
prameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol":   "TSLA",
    "apikey": "a59777d58f4b475083092fa4f49a900f",
}
responce = requests.get(url="https://www.alphavantage.co/query", params=prameters)
responce.raise_for_status()
data = responce.json()
time = TimeHandling(data)
url = ('https://newsapi.org/v2/everything?'
       'q=TSLA&'
       f'from={time.check_last_day_in_list()}&'
       'sortBy=popularity&'
       'apiKey=a59777d58f4b475083092fa4f49a900f')

# Make the request
response1 = requests.get(url)

# Parse the JSON response
news = response1.json()
# Print the entire JSON response (for debugging)

# To print only the articles
articles = news.get('articles', [])
for article in articles:
    Title = f"Title: {article['title']}"
    Description = f"Description: {article['description']}"
    Image = f"{article['urlToImage']}"
    break
