import pandas as pd
from datetime import datetime, timezone
from collections import defaultdict 
import pytz
from Library.Client.Web import Results, Journals, Tasks

def GetExcelDump(start, end, path):
    # timezone: https://stackoverflow.com/questions/1111317/how-do-i-print-a-datetime-in-the-local-timezone
    u_tm = datetime.utcfromtimestamp(0)
    l_tm = datetime.fromtimestamp(0)
    l_tz = timezone(l_tm - u_tm)
    # Calculate usage %
    usage = defaultdict(lambda : 0)
    start = start if not isinstance(start, str) else datetime.strptime(start, '%Y-%m-%d')
    end = end if not isinstance(end, str) else datetime.strptime(end, '%Y-%m-%d')
    start = start.replace(hour=00, minute=00, second=00).replace(tzinfo=l_tz)
    end = end.replace(hour=23, minute=59, second=59).replace(tzinfo=l_tz)
    # Cannot see future time
    now = datetime.now().replace(tzinfo=l_tz)
    end = now if end > now else end
    query=dict(start=start, end=end)
    tasks = Tasks.get_by_query(query)
    results = Results.get_by_query(query)
    journals = Journals.get_by_query(query)
    dfs = [ pd.DataFrame(tasks), pd.DataFrame(results), pd.DataFrame(journals) ]
    for r in results:
        correction = 0
        created = datetime.strptime(r.created, "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=pytz.utc) # DB uses UTC time
        updated = datetime.strptime(r.updated, '%Y-%m-%dT%H:%M:%S.%f').replace(tzinfo=pytz.utc) # DB uses UTC time
        if start > created:
            correction = correction + (start - created).total_seconds()
        if updated > end:
            correction = correction + (updated - end).total_seconds()
        r.duration = (updated - created).total_seconds() - correction
        usage[r.ip] = usage[r.ip] + r.duration
    max_duration = (end - start).total_seconds()
    usage_details = []
    for k,v in usage.items():
        u = dict(IP=k, Available=f'{max_duration:.0f}', Used=f'{v:.2f}', Percentage=f'{v/max_duration * 100:.2f} %')
        usage_details.append(u)
    dfs.append(pd.DataFrame(usage_details))
    # Write to Excel
    with pd.ExcelWriter(path) as writer:
        if not dfs[0].empty: dfs[0].drop(['hosts','results'], axis=1, inplace=True)
        dfs[0].to_excel(writer, sheet_name='Tasks')
        dfs[1].to_excel(writer, sheet_name='Results')
        dfs[2].to_excel(writer, sheet_name='Journals')
        dfs[3].to_excel(writer, sheet_name='Usage')
        writer.save()
    return usage_details