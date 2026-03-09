import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the about section and replace it
# We'll match from <section id="about"> to the next </section>
pattern = r'<section id="about">.*?</section>'

replacement = '''<section id="about">
            <h2>About Me</h2>
            <div class="about-container">
                <div class="about-text">
                    <p><strong>Who I am: </strong>Hi! My name is Abby Hanlon, and I'm a senior at TCU double-majoring in Strategic Communication and Data Analytics, graduating May 2026. I'm a people person, dedicated to creating meaningful relationships wherever I go, with a "can do" attitude.</p>
                    <p><strong>My interests: </strong>I'm a creative communicator, passionate about digital branding, experiential marketing, and storytelling. I've gained hands-on experience through agency, nonprofit, and in-house roles, including graphic design, social media strategy, and event marketing positions. With a strong background in campaign execution, brand development, and content creation, I thrive in fast-paced, collaborative environments where imagination meets strategy.</p>
                    <!-- This section is similar to my LinkedIn profile, to keep it professional, meaningful, and concise for potential employers. -->
                    <p><strong>What I hope to learn: </strong>Throughout this portfolio and the work I accomplish in my final semester as an undergraduate student, I aspire to learn about advanced data visualization, specifically from a design perspective, along with strengthening my "niche" in storytelling and user experience.</p>
                    <!-- I want this section to feel welcoming and warm, with some personalization behind my "about me" story.-->
                </div>
                <div class="about-image">
                    <img src="images/AbbyHanlonHeadshot2026.jpg" alt="Headshot of Abby Hanlon">
                </div>
            </div>
        </section>'''

# Replace
content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully restructured the about section!")
