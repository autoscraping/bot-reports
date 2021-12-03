import report
from constants import Querys, Dict_danblack
import datetime

now_date = datetime.datetime.now()
old_date = now_date - datetime.timedelta(days=2) 
        
initial_date = old_date.strftime('%Y-%m-%d %H:%M:%S')
end_date = now_date.strftime('%Y-%m-%d %H:%M:%S')


query = Querys['danblack']
query_buddi = query.replace('source_page', 'buddi').replace('initial_date', initial_date).replace('end_date', end_date)
query_leafly = query.replace('source_page', 'leafly').replace('initial_date', initial_date).replace('end_date', end_date)
query_dutchie = query.replace('source_page', 'dutchie').replace('initial_date', initial_date).replace('end_date', end_date)

report.report().query(query_dutchie,'dutchie - '+end_date.replace(':','-')+'.csv')
report.report().query(query_leafly,'leafly - '+end_date.replace(':','-')+'.csv')
report.report().query(query_buddi,'buddi - '+end_date.replace(':','-')+'.csv')

