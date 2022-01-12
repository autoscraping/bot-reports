DB_Credentials = {
    'dan-black':{'host': '141.95.47.204',
    'db_name': 'danblack2',
    'user': 'root',
    'password': 'AutoScraping2019',
    'port': '3306'}
}

Querys = {
    'danblack' : "Select \
sou.description as source_name,\
dis.name as Dispensary,\
dis.address as Address,\
dis.city as City,\
dis.lat  as Latitude,\
dis.lon  as Longitude,\
item.source_item_id as source_id,\
item.name as Item,\
item.brand as Brand, \
item.category as Category,\
item.price as Price,\
item.size as Size,\
item.created as scraped_date \
from source as sou \
inner join dispensary as dis \
on dis.source_id = sou.source_id \
inner join item as item \
on item.id_dispensary = dis.id \
where item.created >= 'initial_date' and item.created <= 'end_date' and sou.description = 'source_page' \
order by dis.name ASC;",
    'danblack-clean-dispensary' : "DELETE FROM danblack2.dispensary WHERE dispensary.created <= 'date';",
    'danblack-clean-item' : "DELETE FROM danblack2.item WHERE item.created <= 'date';"
}


Source_danblack = {
    'leafly':'leafly',
    'dutchie':'dutchie',
    'buddi':'buddi',
    'fire & flower':'fire & flower'
}

Dict_danblack = {
    'source_name':'',
    'Dispensary':'',
    'Address':'',
    'City':'',   
    'Latitude':'',
    'source_id':'',
    'Item':'',
    'Brand':'',
    'Category':'',
    'Price':'',
    'Size':'',
    'scraped_date':''
}

