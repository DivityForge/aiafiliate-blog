from transformers import pipeline

# Initialize the GPT-2 pipeline
generator = pipeline('text-generation', model='distilgpt2')

# Prompt for generating CSS
prompt = "Generate modern, minimalist CSS for an affiliate blog. Include readable fonts, spacious layout, and pastel colors."

# Generate CSS content
css_content = generator(prompt, max_length=300)[0]['generated_text']

# Save generated CSS to style.css file
with open("assets/css/style.css", "w") as css_file:
    css_file.write(css_content)
