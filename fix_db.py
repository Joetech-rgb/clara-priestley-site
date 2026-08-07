import re

path = r".\lawfirm\settings.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r"DATABASES = \{.*?\n\}\n", re.DOTALL)
new_block = "DATABASES = {\n    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))\n}\n"

new_content, count = pattern.subn(new_block, content, count=1)

if count:
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("DATABASES block replaced:", count)
else:
    print("WARNING: pattern still not found")
