def discover_top_niches(k=5):
    # Static seed niches to avoid API errors
    seeds = ["home office", "remote work", "eco travel", "pet care", "smart home"]
    return seeds[:k]
