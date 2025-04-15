# scripts/style_update.py
with open('assets/css/style.scss', 'r') as file:
    css = file.read()

# Example CSS modification (change font)
css = css.replace('font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;', 'font-family: "Roboto", sans-serif;')

with open('assets/css/style.scss', 'w') as file:
    file.write(css)

print("CSS style updated successfully!")
