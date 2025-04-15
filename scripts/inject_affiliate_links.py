import os
from datetime import datetime

# Configuration
POSTS_DIR = "_posts"
AFFILIATE_ID = "divityforge84-20"

# Simple keyword-to-product mapping
AFFILIATE_KEYWORDS = {
    "desk": "https://www.amazon.com/dp/B08L5W2M3N?tag=divityforge84-20",
    "keyboard": "https://www.amazon.com/dp/B07FZ8S74R?tag=divityforge84-20",
    "headphones": "https://www.amazon.com/dp/B07QKQJL17?tag=divityforge84-20"
}

def inject_links_in_post(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()

    content = "".join(lines)
    updated = False
    injected_section = "\n\n## 🔗 Recommended Products\n"

    for keyword, link in AFFILIATE_KEYWORDS.items():
        if keyword in content and link not in content:
            updated = True
            injected_section += f"- If you liked this post, check out this [{keyword} on Amazon]({link})\n"

    # If we added anything, append it to the post
    if updated:
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(injected_section)
        print(f"✅ Injected affiliate links into: {filepath}")
    else:
        print(f"🟡 No update needed for: {filepath}")

def main():
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            inject_links_in_post(os.path.join(POSTS_DIR, filename))

if __name__ == "__main__":
    print(f"🔍 Starting affiliate link injection at {datetime.now()}")
    main()
