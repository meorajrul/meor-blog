"""Fetch reproducible NVD publication counts and October records, no API key.
Snapshot ends at 21 October 2026 23:59:59.999 UTC: complete days only.
"""
from pathlib import Path
import calendar,datetime as dt,json,time,requests,hashlib
BASE=Path(__file__).resolve().parent
RAW=BASE/'raw'; RAW.mkdir(exist_ok=True)
API='https://services.nvd.nist.gov/rest/json/cves/2.0'
session=requests.Session()
def fetch(name,params):
 path=RAW/(name+'.json')
 if path.exists():return json.loads(path.read_text())
 for attempt in range(3):
  try:
   r=session.get(API,params=params,timeout=35)
  except requests.RequestException as e:
   print(name,type(e).__name__,flush=True);time.sleep(8);continue
  if r.status_code==200:
   data=r.json();path.write_text(json.dumps(data,ensure_ascii=False))
   meta=dict(request_url=r.url,retrieved_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(),api_timestamp=data.get('timestamp'),sha256=hashlib.sha256(path.read_bytes()).hexdigest())
   (RAW/(name+'-request.json')).write_text(json.dumps(meta,indent=2))
   print(name,data['totalResults'],flush=True);time.sleep(6.3);return data
  print(name,'HTTP',r.status_code,flush=True);time.sleep(8*(attempt+1))
 raise RuntimeError(f'Unable to retrieve {name}; no substitute values permitted')
monthly=[]
for month in range(1,11):
 day=21 if month==10 else calendar.monthrange(2026,month)[1]
 params=dict(pubStartDate=f'2026-{month:02}-01T00:00:00.000Z',pubEndDate=f'2026-{month:02}-{day:02}T23:59:59.999Z',resultsPerPage=1,noRejected='')
 d=fetch(f'month-{month:02}',params)
 monthly.append(dict(month=f'2026-{month:02}',count=d['totalResults'],partial=month==10,api_timestamp=d['timestamp']))
(BASE/'monthly-counts.json').write_text(json.dumps(monthly,indent=2))
daily=[]
for day in range(1,22):
 d=fetch(f'day-{day:02}',dict(pubStartDate=f'2026-10-{day:02}T00:00:00.000Z',pubEndDate=f'2026-10-{day:02}T23:59:59.999Z',resultsPerPage=1,noRejected=''))
 daily.append(dict(date_utc=f'2026-10-{day:02}',count=d['totalResults'],api_timestamp=d['timestamp']))
(BASE/'daily-counts.json').write_text(json.dumps(daily,indent=2))
assert sum(x['count'] for x in daily)==monthly[-1]['count'], 'Snapshot changed during fetch; reconcile before charting'
print('COMPLETE',sum(m['count'] for m in monthly),'YTD;',monthly[-1]['count'],'October',flush=True)
