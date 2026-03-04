import pandas as pd
import folium
from folium import Icon, Marker
import requests
import time

# Configuration
MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoiYWJieWhhbmxvbiIsImEiOiJjbWx0cW9tdmgwMzZwM2duNXpqM3k5MmU3In0.5XpzgzufR5FXSMfl0VW76A'
MAPBOX_STYLE_URL = 'abbyhanlon/cmmb8ae9u005o01s5e9rj3hn9'

# ===== CUSTOMIZATION SECTION =====
# Update these colors to match your Mapbox design theme
POPUP_ACCENT_COLOR = '#4a90e2'  # Border color in popups - change to match your basemap
POPUP_TEXT_COLOR = '#1a1a1a'    # Header text color
POPUP_BODY_COLOR = '#333'       # Description text color

# Define color scheme for different location types
TYPE_COLORS = {
    'Cultural / Historical': 'red',
    'Recreation / Park': 'green',
    'School': 'blue',
    'Coffee Shop': 'brown',
    'Park / Recreation': 'green',
    'Park / Nature': 'darkgreen',
    'Cultural / Community': 'orange',
    'Recreation / Golf': 'lightgreen',
    'Nature / Conservation': 'darkgreen',
    'Park / Historical': 'lightred',
    'Cultural / Education': 'purple',
    'Recreation': 'green',
    'Nature': 'darkgreen',
    'Historical': 'red',
    'Transportation / Landmark': 'gray',
    'Boutique / Local Shop': 'pink',
    'Pub / Bar': 'darkred',
    'Park': 'green',
    'Recreation / Marina': 'lightblue',
    'Religious / Landmark': 'cadetblue',
    'Event / Cultural': 'orange',
    'American / Bistro': 'beige',
    'Fine Dining / American': 'lightred',
    'Italian': 'red',
    'Steakhouse / American': 'darkred',
    'American / Contemporary': 'orange',
    'Cafe / Breakfast & Lunch': 'beige',
    'Japanese / Sushi': 'red',
    'Brew Pub / Bar': 'darkred',
    'Pub / Bar Food': 'darkred',
    'Mexican': 'orange',
    'Italian / Pizza': 'red',
    'Pizza / Italian': 'red',
    'Restaurant / Hotel': 'lightred',
    'Historical / Cultural': 'red',
    'Recreation / Community': 'lightgreen',
    'Cultural': 'orange'
}

# Define icons for different categories
def get_icon_for_type(location_type):
    """Return appropriate icon based on location type"""
    type_lower = location_type.lower()
    
    if 'park' in type_lower or 'nature' in type_lower or 'recreation' in type_lower:
        return 'tree'
    elif 'school' in type_lower:
        return 'book'
    elif 'coffee' in type_lower or 'cafe' in type_lower:
        return 'coffee'
    elif 'restaurant' in type_lower or 'dining' in type_lower or 'food' in type_lower or 'pizza' in type_lower or 'bistro' in type_lower or 'sushi' in type_lower or 'italian' in type_lower or 'mexican' in type_lower or 'steakhouse' in type_lower:
        return 'cutlery'
    elif 'pub' in type_lower or 'bar' in type_lower:
        return 'glass'
    elif 'cultural' in type_lower or 'historical' in type_lower:
        return 'university'
    elif 'church' in type_lower or 'religious' in type_lower:
        return 'home'
    elif 'shop' in type_lower or 'boutique' in type_lower:
        return 'shopping-cart'
    elif 'train' in type_lower or 'transportation' in type_lower:
        return 'train'
    elif 'beach' in type_lower or 'marina' in type_lower or 'yacht' in type_lower:
        return 'ship'
    else:
        return 'info-sign'

def geocode_address(address, mapbox_token):
    """
    Geocode an address using Mapbox Geocoding API
    Returns (latitude, longitude) tuple or None if failed
    """
    base_url = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    
    # URL encode the address
    encoded_address = requests.utils.quote(address)
    url = f"{base_url}/{encoded_address}.json?access_token={mapbox_token}&limit=1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data['features']:
            coordinates = data['features'][0]['geometry']['coordinates']
            # Mapbox returns [longitude, latitude], so we need to reverse it
            return (coordinates[1], coordinates[0])
        else:
            print(f"No results found for address: {address}")
            return None
    except Exception as e:
        print(f"Error geocoding {address}: {e}")
        return None

def create_popup_html(name, description, image_url):
    """Create HTML for popup with image, name, and description"""
    html = f"""
    <div style="width: 320px; font-family: 'Helvetica Neue', Arial, sans-serif;">
        <h3 style="margin: 0 0 12px 0; 
                   color: {POPUP_TEXT_COLOR}; 
                   font-size: 18px;
                   font-weight: 600;
                   border-bottom: 3px solid {POPUP_ACCENT_COLOR}; 
                   padding-bottom: 8px;">
            {name}
        </h3>
        <img src="{image_url}" 
             alt="{name}" 
             style="width: 100%; 
                    height: 200px; 
                    object-fit: cover; 
                    border-radius: 8px; 
                    margin-bottom: 12px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);"
             onerror="this.style.display='none'">
        <p style="font-size: 14px; 
                  line-height: 1.6; 
                  color: {POPUP_BODY_COLOR}; 
                  margin: 0;
                  text-align: justify;">
            {description}
        </p>
    </div>
    """
    return folium.Popup(html, max_width=350)

def create_hometown_map(csv_file, mapbox_token, mapbox_style_url, output_html='hometown_map.html'):
    """
    Main function to create the interactive map
    
    Args:
        csv_file: Path to CSV file with location data
        mapbox_token: Mapbox access token
        mapbox_style_url: URL to your custom Mapbox style
        output_html: Output filename for the HTML map
    """
    # Read the CSV file
    print(f"Reading CSV file: {csv_file}")
    df = pd.read_csv(csv_file)
    
    # Display data info
    print(f"Loaded {len(df)} locations")
    print(f"Location types: {df['Type'].unique()}")
    
    # Create base map centered on Lake Forest, IL
    # Using approximate center coordinates
    center_lat, center_lon = 42.2587, -87.8406
    
    # Create the map with Mapbox tiles
    # Construct the tile URL with your Mapbox style
    tile_url = f'https://api.mapbox.com/styles/v1/{mapbox_style_url}/tiles/{{z}}/{{x}}/{{y}}?access_token={mapbox_token}'
    
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=13,
        tiles=tile_url,
        attr='Map data &copy; <a href="https://www.mapbox.com/">Mapbox</a>'
    )
    
    # Track geocoding statistics
    successful = 0
    failed = 0
    
    # Process each location
    for idx, row in df.iterrows():
        print(f"\nProcessing {idx + 1}/{len(df)}: {row['Name']}")
        
        # Geocode the address
        coords = geocode_address(row['Address'], mapbox_token)
        
        if coords:
            lat, lon = coords
            successful += 1
            
            # Get color and icon for this location type
            color = TYPE_COLORS.get(row['Type'], 'blue')
            icon_name = get_icon_for_type(row['Type'])
            
            # Create popup
            popup = create_popup_html(row['Name'], row['Description'], row['Image_URL'])
            
            # Add marker to map
            folium.Marker(
                location=[lat, lon],
                popup=popup,
                tooltip=row['Name'],
                icon=folium.Icon(color=color, icon=icon_name, prefix='glyphicon')
            ).add_to(m)
            
            print(f"✓ Added marker at ({lat:.4f}, {lon:.4f})")
        else:
            failed += 1
            print(f"✗ Failed to geocode")
        
        # Add a small delay to respect API rate limits
        time.sleep(0.1)
    
    # Add a legend to the map
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; right: 50px; width: 220px; height: auto; 
                background-color: white; z-index:9999; font-size:14px;
                border:2px solid grey; border-radius: 5px; padding: 10px">
    <h4 style="margin-top:0;">Location Types</h4>
    <p><i class="glyphicon glyphicon-tree" style="color:green"></i> Parks & Nature</p>
    <p><i class="glyphicon glyphicon-book" style="color:blue"></i> Schools</p>
    <p><i class="glyphicon glyphicon-cutlery" style="color:red"></i> Restaurants</p>
    <p><i class="glyphicon glyphicon-coffee" style="color:brown"></i> Coffee Shops</p>
    <p><i class="glyphicon glyphicon-glass" style="color:darkred"></i> Pubs & Bars</p>
    <p><i class="glyphicon glyphicon-university" style="color:orange"></i> Cultural Sites</p>
    <p><i class="glyphicon glyphicon-ship" style="color:lightblue"></i> Waterfront</p>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Save the map
    m.save(output_html)
    
    print(f"\n{'='*50}")
    print(f"Map creation complete!")
    print(f"Successful geocoding: {successful}")
    print(f"Failed geocoding: {failed}")
    print(f"Map saved to: {output_html}")
    print(f"{'='*50}")
    
    return m

if __name__ == "__main__":
    # Replace these with your actual Mapbox credentials
    if MAPBOX_ACCESS_TOKEN == 'YOUR_MAPBOX_ACCESS_TOKEN_HERE':
        print("⚠️  WARNING: Please set your MAPBOX_ACCESS_TOKEN in the script!")
        print("You can get a token at: https://account.mapbox.com/access-tokens/")
        print("\nFor now, using a basic map without custom style...")
        # Use basic OpenStreetMap tiles as fallback
        csv_file = 'hometown_locations.csv - Lake Forest Places.csv'
        df = pd.read_csv(csv_file)
        
        # Create basic map
        m = folium.Map(location=[42.2587, -87.8406], zoom_start=13)
        
        print("\n⚠️  Geocoding requires a Mapbox token. Please add your token to use this feature.")
    else:
        # Run the main function with your settings
        create_hometown_map(
            csv_file='hometown_locations.csv - Lake Forest Places.csv',
            mapbox_token=MAPBOX_ACCESS_TOKEN,
            mapbox_style_url=MAPBOX_STYLE_URL,
            output_html='hometown_map.html'
        )
