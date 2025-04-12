import json
from transformers import pipeline

def generate_articles(niches, count=4):
    gen = pipeline("text-generation", model="bigscience/bloom", device="cpu")
    for i in range(count):
        niche = niches[i % len(niches)]
        prompt = (
            f"Write an 800‑word SEO‑optimized blog post about {niche}. "
            "Include two affiliate product recommendations with brief pros and cons."
        )
        text = gen(prompt, max_length=1000)[0]["generated_text"]
        filename = f"content/{niche.replace(' ','-')}-{i+1}.md"
        with open(filename, "w") as f:
            f.write(f"---\ntitle: \"{niche.title()} Guide #{i+1}\"\n---\n\n")
            f.write(text)
