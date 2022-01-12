import report
from constants import Querys, Dict_danblack
import datetime

now_date = datetime.datetime.now()

#formating date for generate reports
old_date = now_date - datetime.timedelta(days=2) 
        
initial_date = old_date.strftime('%Y-%m-%d %H:%M:%S')
end_date = now_date.strftime('%Y-%m-%d %H:%M:%S')


query = Querys['danblack']
#formating query for each report
query.replace('initial_date', initial_date).replace('end_date', end_date) 
query_buddi = query.replace('source_page', 'buddi')
query_leafly = query.replace('source_page', 'leafly')
query_dutchie = query.replace('source_page', 'dutchie')
query_fireAndFlowers = query.replace('source_page', 'fire & flower')
query_valuebuds = query.replace('source_page', 'Value buds')


report.report().query_report(query_dutchie,'dutchie - '+end_date.replace(':','-')+'.csv')
report.report().query_report(query_leafly,'leafly - '+end_date.replace(':','-')+'.csv')
report.report().query_report(query_buddi,'buddi - '+end_date.replace(':','-')+'.csv')
#report.report().query_report(query_fireAndFlowers,'fire & flower - '+end_date.replace(':','-')+'.csv')
report.report().query_report(query_valuebuds,'Value buds - '+end_date.replace(':','-')+'.csv')

#formating date for clean dbs
date_clean = (now_date - datetime.timedelta(days=12)).strftime('%Y-%m-%d %H:%M:%S')

query_clean = Querys['danblack-clean-dispensary'].replace('date',date_clean)
report.report().query_clean_db(query_clean)
query_clean = Querys['danblack-clean-item'].replace('date',date_clean)
report.report().query_clean_db(query_clean)
