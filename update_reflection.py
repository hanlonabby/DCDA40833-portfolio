#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The new HTML structure for the reflection section
new_html = '''        <!-- Reflection Section: Optional semester reflection -->
        <section id="reflection">
            <h2>Semester Reflection</h2>
            
            <div class="reflection-collapsible">
                <button class="reflection-header">
                    What I Learned
                    <span class="collapsible-icon">▼</span>
                </button>
                <div class="reflection-content">
                    <div class="reflection-inner">
                        <p>I've learned the importance of starting off strong with organization within code, and how you practice it. Keeping your VS Code space clean and easy to read is one of the most vital skills in learning how to develop a website.</p>
                        <p><em>Add more details about what you learned throughout the semester...</em></p>
                    </div>
                </div>
            </div>

            <div class="reflection-collapsible">
                <button class="reflection-header">
                    Challenges I Overcame
                    <span class="collapsible-icon">▼</span>
                </button>
                <div class="reflection-content">
                    <div class="reflection-inner">
                        <p>I'm having the most trouble being creative with my color schemes and beginning the initial stages of brainstorming what I want to make of this portfolio. I know that struggling with color schemes might seem kind of silly. Still, I'm passionate about a fair user experience and about creating a website that feels welcoming, engaging, and artistic.</p>
                        <p><em>Add more details about the challenges you faced and overcame...</em></p>
                    </div>
                </div>
            </div>

            <div class="reflection-collapsible">
                <button class="reflection-header">
                    How I Grew
                    <span class="collapsible-icon">▼</span>
                </button>
                <div class="reflection-content">
                    <div class="reflection-inner">
                        <p><em>Paste your reflection on how your understanding of digital culture and data analytics evolved...</em></p>
                    </div>
                </div>
            </div>

            <div class="reflection-collapsible">
                <button class="reflection-header">
                    Looking Ahead
                    <span class="collapsible-icon">▼</span>
                </button>
                <div class="reflection-content">
                    <div class="reflection-inner">
                        <p><em>Paste your thoughts on how you'll apply these skills in the future...</em></p>
                    </div>
                </div>
            </div>
        </section>'''

# Find the start and end of the reflection section
start_marker = '        <!-- Reflection Section: Optional semester reflection -->'
end_marker = '        </section>\n    </main>'

start_idx = content.find(start_marker)
if start_idx == -1:
    print("ERROR: Could not find start marker")
    exit(1)

# Find the </section> that belongs to the reflection section
temp_idx = start_idx
section_end_idx = -1
for i in range(10):  # Try to find the next few </section> tags
    temp_idx = content.find('        </section>', temp_idx + 1)
    if temp_idx == -1:
        break
    # Check if the next text is '</main>'
    next_text = content[temp_idx:temp_idx + 30]
    if '</section>\n    </main>' in next_text:
        section_end_idx = temp_idx
        break

if section_end_idx == -1:
    print("ERROR: Could not find end marker")
    exit(1)

# Replace the old section with the new one
new_content = content[:start_idx] + new_html + content[section_end_idx + len('        </section>'):]

# Write the updated content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✓ Successfully updated Semester Reflection section with collapsible dropdowns!")
