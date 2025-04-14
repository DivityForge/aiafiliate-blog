import os, datetime
from transformers import pipeline

def generate_articles(niches, count=4):
    gen = pipeline("text-generation", model="distilgpt2", device="cpu")
    os.makedirs("content/posts", exist_ok=True)
    for niche in niches:
        for i in range(count):
            title = f"{niche.title()} Insights #{i+1}"
            date = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
            prompt = f"Write an 800‑word SEO‑optimized blog post about {niche}. Include two affiliate product recommendations with brief pros and cons."
            text = gen(prompt, max_length=300)[0]["generated_text"]
            filename = f"content/posts/{niche.replace(' ','-')}-{i+1}.md"
            with open(filename, "w") as f:
                f.write(f"---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"date: {date}\n")
                f.write(f"draft: false\n")
                f.write(f"---\n\n")
                f.write(text)
