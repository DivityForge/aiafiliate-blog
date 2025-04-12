from pytrends.request import TrendReq

def discover_top_niches(k=5):
    py = TrendReq()
    seeds = ["home office", "remote work", "eco travel", "pet care", "smart home"]
    trends = py.trending_searches(pn="united_states").head(10).tolist()
    return trends[:k]
