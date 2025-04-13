import logging
logging.basicConfig(level=logging.INFO)
import json
from transformers import pipeline

def generate_articles(niches, count=3):
    from transformers import pipeline
    generator = pipeline("text-generation", model="distilgpt2")  # Small and fast

    for niche in niches:
        logging.info(f"▶️ Generating articles for niche: {niche}")
        for i in range(count):
            try:
                prompt = f"Write a short blog post about {niche}."
                out = generator(prompt, max_length=300, num_return_sequences=1, do_sample=True)[0]['generated_text']
                # save to markdown
                filename = f"content/{niche.replace(' ', '-')}-{i+1}.md"
                with open(filename, "w") as f:
                    f.write(f"# {niche.title()} Article {i+1}\n\n{out}")
                logging.info(f"✅ Saved {filename}")
            except Exception as e:
                logging.error(f"❌ Error generating article {i+1} for {niche}: {e}")
