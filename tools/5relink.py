import os
import re

relpat = re.compile(r'href="(\.\./.*/)([-a-z0-9])+/"')

for file in os.listdir("."):
    if file.endswith(".md") and file != 'README.md':
        with open(file, 'r') as f:
            content = f.read()
            match = relpat.search(content)
            updated = False
            while match:
                updated = True
                content = content.replace(match.group(), match.group(1) + ".md")
                match = relpat.search(content)
        with open(file, 'w') as f:
            f.write(content)
