import os

from metaappscriptsdk import MetaApp

META = MetaApp()
log = META.log

os.chdir(os.path.dirname(os.path.abspath(__file__)))
__DIR__ = os.getcwd() + "/"

q = """
SELECT
  engine as platform,
  campaign_remote_id,
  SUM(impressions) as impressions,
  SUM(clicks) as clicks,
  ROUND(SUM(cost), 3) as cost
FROM adplatform.campaign_stats_report
WHERE stat_date BETWEEN '2017-02-01' AND '2017-03-31'
AND engine = 'banner'
GROUP BY platform, campaign_remote_id
ORDER BY platform, campaign_remote_id
"""

configuration = {
    "download": {
        # "skipHeaders": True,
        "dbQuery": {
            "command": q,
        }
    }
}
metaql = META.MetaqlService
resp = metaql.download_data(configuration, output_file=__DIR__ + 'assets/stat.tsv')
log.info("end")
