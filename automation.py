import os, shutil, re, requests

# 1. Move JPG
os.makedirs("source_folder", exist_ok=True)
os.makedirs("jpg_folder", exist_ok=True)
for file in os.listdir("source_folder"):
    if file.lower().endswith(".jpg"):
        shutil.move(f"source_folder/{file}", f"jpg_folder/{file}")
print("JPG files moved")

# 2. Extract Emails
with open("sample.txt","w") as f:
    f.write("Email us at support@codealpha.tech and nayan@gmail.com")
with open("sample.txt") as f:
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', f.read())
with open("emails.txt","w") as f:
    f.write("\n".join(emails))
print(f"Emails found: {emails}")

# 3. Scrape Title
res = requests.get("https://www.python.org")
title = re.search(r'<title>(.*?)</title>', res.text).group(1)
with open("web_title.txt","w") as f:
    f.write(title)
print(f"Website Title: {title}")