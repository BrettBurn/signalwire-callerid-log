# SignalWire-CallerId-Log
This code snippet will allow for easy logging of Caller ID on inbound calls into a SignalWire user's pre-existing call logs.

# Packages and External Dependencies
For this code to work, you will need to have a few different packages installed. In this code, you will need pandas, datetime, and the SignalWire Python SDK installed. 

* Read here on how to install [Pandas](https://developer.signalwire.com/apis/docs/list-calls-to-csv-all-languages)
* Read here on how to install [datetime](https://developer.signalwire.com/apis/docs/list-calls-to-csv-all-languages)
* Read here on how to install the [SignalWire Python SDK](https://developer.signalwire.com/apis/docs/list-calls-to-csv-all-languages)

# How the Script Works
First, let's import the necessary resources, including datetime, pandas, and the SignalWire Client. After we do this, we'll need to instantiate the SignalWire client. We do this by using our API credentials that you can find under your API section of your SignalWire Space. These credentials include your `ProjectID`, `AuthToken`, and `signalwire_space_url`. 

```python
from datetime import datetime
from signalwire.rest import Client as signalwire_client
import pandas as pd

client = signalwire_client("ProjectID", "AuthToken", signalwire_space_url = 'SpaceURL')
```

We then choose what the parameters you'd like to filter by. In this example, we've filtered by a date range. This is where datetime comes in handy. The order for these arguments is Year, Month, Day, Hour, Minute, and Second. Unless you need this script to run in a very specific manner, we can leave the script's Hour, Minute, and Second attributes at `0`. We also filter by the `completed` status to only show calls that were initiated, connected, in progress, and ended successfully. 

```python
calls = client.calls.list(start_time_after=datetime(2021, 0o1, 24, 0, 0, 0), start_time_before=datetime(2021, 0o1, 27, 0, 0, 0), status='completed')
```
Next we insert the data from the calls into an empty array, which is assigned as the variable `d` in this script. By the end, we'll append all the parameters you wish to into this array. Notice that `record.caller_name` is a parameter in this function. If Caller ID Lookup is enabled on your account (which you can get by opening a ticket with SignalWire's Support Team), it will list the Caller ID in this array as well. 

```python
d = []

# Appends all data from calls into an array
for record in calls:
    d.append((record.from_formatted, record.to_formatted, record.start_time, record.caller_name, record.sid))

print(d)
```

Next, we need to format the array into something more legible, complete with a table of rows and columns to make this data easier to read. It's important to make sure that the order of the headers match up with the parameters you pull from the API in the portion of the script above. For example, notice that the `from_formatted` parameter above is the first attribute called in the function above. In the portion of the script below, `From` is the first column to be created.

```python
df = pd.DataFrame(d, columns=('From', 'To', 'Date', 'Status', 'CallSID'))

print('dataframe')
print('\n')
print(df)
```

While not completely necessary to see your logs, you can export the entire log to a CSV file if you would like using the final line of code here. 

```python
df.to_csv('calls.csv', index=False, encoding='utf-8')
```
