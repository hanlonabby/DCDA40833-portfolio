
<!-- AI gave me a step-by-step walkthrough of how to add an image to my carousel guide that it created for me -->
# Image Carousel Guide

## How to Add Your Own Images

### Step 1: Prepare Your Images
- Save your images in the `images/` folder
- Recommended image size: 1200px x 800px (or similar 3:2 ratio)
- Supported formats: JPG, PNG, WebP
- Name your images something descriptive (e.g., `project1.jpg`, `design-work.jpg`)

### Step 2: Update the HTML
Open `index.html` and find the carousel section (around line 65). For each slide, update:

```html
<div class="carousel-slide">
    <img src="images/YOUR-IMAGE-NAME.jpg" alt="Descriptive alt text">
    <div class="carousel-caption">
        <h3>Your Image Title</h3>
        <p>Your image description goes here.</p>
    </div>
</div>
```

### Step 3: Add More Slides
To add additional slides, copy this structure:

```html
<!-- New Slide -->
<div class="carousel-slide">
    <img src="images/your-image.jpg" alt="Description">
    <div class="carousel-caption">
        <h3>Title</h3>
        <p>Description</p>
    </div>
</div>
```

**Important:** When you add a new slide, also add a new indicator dot:

```html
<button class="indicator" aria-label="Go to slide 4"></button>
```

### Step 4: Customize the Carousel
You can customize the carousel behavior in the JavaScript section:
- **Auto-play speed:** Change `5000` (milliseconds) in line ~223 to adjust how long each slide displays
- **Remove auto-play:** Comment out or delete the `startAutoPlay()` call at the bottom

### Features Included:
✅ Auto-advances every 5 seconds  
✅ Pauses on hover  
✅ Previous/Next buttons  
✅ Indicator dots to jump to specific slides  
✅ Keyboard navigation (arrow keys)  
✅ Mobile responsive  
✅ Dark mode compatible  

### Placeholder Images
The carousel currently uses placeholder images:
- `images/placeholder1.jpg`
- `images/placeholder2.jpg`
- `images/placeholder3.jpg`

Replace these with your actual images when ready!
