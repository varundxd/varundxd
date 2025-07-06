import random

# Load fun facts
with open("fun_facts.txt", "r", encoding="utf-8") as f:
    facts = [line.strip() for line in f if line.strip()]

# Pick a random fact
selected_fact = random.choice(facts)

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace between markers
start = "<!--START_FUN_FACT-->"
end = "<!--END_FUN_FACT-->"
before = content.split(start)[0]
after = content.split(end)[1]

new_section = f"{start}\n> 💡 {selected_fact}\n{end}"
updated = before + new_section + after

# Save
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
