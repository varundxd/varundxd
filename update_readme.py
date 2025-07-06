import random

# Load fun facts
with open("fun_facts.txt", "r", encoding="utf-8") as f:
    facts = [line.strip() for line in f if line.strip()]

# Pick a random fact
selected_fact = random.choice(facts)

# Read README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace placeholder section
start = "<!--START_FUN_FACT-->"
end = "<!--END_FUN_FACT-->"
new_content = content.split(start)[0] + start + "\n" + f"> 💡 {selected_fact}\n" + end + content.split(end)[1]

# Write back updated content
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
