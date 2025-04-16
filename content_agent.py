import os
import datetime
from transformers import pipeline

def generate_articles(niches, count=1):
    gen = pipeline("text-generation", model="distilgpt2", device="cpu")
    os.makedirs("_posts", exist_ok=True)
    for niche in niches:
        for i in range(count):
            title = f"{niche.title()} Insights #{i+1}"
            date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
            prompt = f"Write an 800‑word SEO‑optimized blog post about {niche}. Include two affiliate product recommendations with brief pros and cons."
            text = gen(prompt, max_length=300)[0]["generated_text"]

            safe_niche = niche.lower().replace(" ", "-")
            filename = f"_posts/{date}-{safe_niche}-{i+1}.md"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"date: {date}\n")
                f.write(f"layout: post\n")
                f.write(f"draft: false\n")
                f.write(f"---\n\n")
                f.write(text)

# Example usage
niches = ["smart home"]
generate_articles(niches)
