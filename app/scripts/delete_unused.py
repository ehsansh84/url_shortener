from publics import db
from datetime import datetime, timedelta
col = db()['url']
# For ease of test it set to 1 day, It can be easily set to 1 year
from_date = datetime.utcnow() - timedelta(days=1)

query = {"updated_at": {"$lt": from_date}}

# For test purpose you can see urls to delete here
for item in col.find(query):
    print(item)

# If you uncomment this code, urls older than 1 day will be deleted
# col.delete_many(query)
