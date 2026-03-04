# Lake Forest Hometown Map - Setup Guide

## Overview
This script creates an interactive map of Lake Forest locations with custom markers, pop-ups with images, and geocoding using the Mapbox API.

## Prerequisites
The required packages are already installed:
- `folium` - for creating interactive maps
- `pandas` - for reading CSV data
- `requests` - for API calls

## Setup Instructions

### 1. Get Your Mapbox Access Token

1. Go to [https://account.mapbox.com/](https://account.mapbox.com/)
2. Sign up or log in to your account
3. Navigate to **Access Tokens** 
4. Copy your default public token OR create a new one

### 2. Create Your Custom Mapbox Style (Optional)

1. Log in to Mapbox Studio: [https://studio.mapbox.com/](https://studio.mapbox.com/)
2. Click **New Style** or use an existing style
3. Customize your map (colors, labels, etc.)
4. Once done, click **Share** and copy the **Style URL**
   - It will look like: `username/style-id` or `mapbox/streets-v12`

### 3. Configure the Script

Open `hometown_map.py` and replace these two lines:

```python
MAPBOX_ACCESS_TOKEN = 'YOUR_MAPBOX_ACCESS_TOKEN_HERE'  # Paste your token here
MAPBOX_STYLE_URL = 'YOUR_MAPBOX_STYLE_URL_HERE'  # e.g., 'mapbox/streets-v12' or 'yourusername/abc123'
```

Example:
```python
MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoiamFuZWRvZSIsImEiOiJjbHlhYmMxMjMifQ.abcdefghijk'
MAPBOX_STYLE_URL = 'mapbox/outdoors-v12'
```

### 4. Run the Script

```bash
python hometown_map.py
```

The script will:
- ✅ Read the CSV file with 50+ Lake Forest locations
- ✅ Geocode each address using Mapbox API
- ✅ Create markers with custom colors and icons based on location type
- ✅ Add interactive pop-ups with images and descriptions
- ✅ Save the map as `hometown_map.html`

### 5. View Your Map

Open `hometown_map.html` in your web browser to see the interactive map!

## Features

### Color-Coded Markers
- 🟢 **Green**: Parks & Recreation
- 🔵 **Blue**: Schools
- 🔴 **Red**: Restaurants & Cultural Sites
- 🟤 **Brown**: Coffee Shops
- 🟥 **Dark Red**: Pubs & Bars
- 🟧 **Orange**: Cultural/Community Centers

### Interactive Elements
- **Hover** over markers to see location names
- **Click** markers to see:
  - Location images
  - Personal descriptions
  - Location names

### Location Types Covered
- Parks & Nature Preserves
- Schools & Educational Institutions
- Restaurants & Dining
- Coffee Shops & Cafes
- Cultural & Historical Sites
- Recreation Centers
- Pubs & Bars
- And more!

## Customization Options

### Change Map Center or Zoom
In the `create_hometown_map()` function:
```python
m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=13,  # Change zoom level (1-18)
)
```

### Modify Marker Colors
Edit the `TYPE_COLORS` dictionary:
```python
TYPE_COLORS = {
    'Cultural / Historical': 'red',  # Change to any Folium color
    'Recreation / Park': 'green',
    # ... add more types
}
```

### Change Icons
Modify the `get_icon_for_type()` function to use different [Bootstrap Glyphicons](https://getbootstrap.com/docs/3.3/components/#glyphicons)

### Adjust Popup Width
In `create_popup_html()`:
```python
return folium.Popup(html, max_width=320)  # Change width
```

## Troubleshooting

### "No results found for address"
- The address might be incorrect or not recognized by Mapbox
- Check the CSV file for typos in addresses

### Map displays but markers don't appear
- Check that your Mapbox token is valid
- Ensure you haven't exceeded the free tier limit (100,000 requests/month)

### Images don't load in popups
- Check that Image_URL values in the CSV are valid
- Some images may be blocked by CORS policies

### Rate Limiting
The script includes a 0.1-second delay between API calls. If you hit rate limits, increase the delay:
```python
time.sleep(0.5)  # Increase from 0.1 to 0.5 seconds
```

## API Rate Limits (Mapbox Free Tier)
- **Geocoding**: 100,000 requests/month
- **Map Loads**: 200,000 per month
- This script makes 1 geocoding request per location (50+ total)

## Output Files
- `hometown_map.html` - Interactive map (open in any browser)

## Next Steps
- Share your map by hosting the HTML file on GitHub Pages
- Customize the Mapbox style to match your preferences
- Add more locations to your CSV file

## Support
For Mapbox documentation:
- [Geocoding API](https://docs.mapbox.com/api/search/geocoding/)
- [Static Tiles API](https://docs.mapbox.com/api/maps/static-tiles/)
- [Mapbox Studio](https://docs.mapbox.com/studio-manual/)

For Folium documentation:
- [Folium Quickstart](https://python-visualization.github.io/folium/quickstart.html)
