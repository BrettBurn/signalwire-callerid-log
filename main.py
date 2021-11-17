from datetime import datetime
from signalwire.rest import Client as signalwire_client
import pandas as pd

client = signalwire_client("ProjectID", "AuthToken", signalwire_space_url = 'example.signalwire.com')


calls = client.calls.list(start_time_after=datetime(2021, 0o1, 24, 0, 0, 0), start_time_before=datetime(2021, 11, 27, 0, 0, 0), status='completed')

d = []


for record in calls:
    d.append((record.from_formatted, record.to_formatted, record.start_time, record.status, record.sid, record.caller_name))

print(d)


df = pd.DataFrame(d, columns=('From', 'To', 'Date', 'Status', 'CallSID', 'CallerID'))

print('dataframe')
print('\n')
print(df)

df.to_csv('callerid.csv', index=False, encoding='utf-8')
