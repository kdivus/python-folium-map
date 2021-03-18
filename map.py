import folium
import os 
import json

#create map object
m = folium.Map(location=[45.8153, 15.9665, ], zoom_start=12)

# global tooltip
tooltip = 'Click For More Info'

#create custom marker icon
logoIcon = folium.features.CustomIcon('logo.jpg', icon_size=(150, 90))

#vega data
vis = os.path.join('data', 'vis.json')

#geojson data
overlay = os.path.join('data', 'overlay.json')


#create markers
folium.Marker([45.8484, 15.9989],popup='<strong>Location One</strong>',
              tooltip=tooltip,).add_to(m),
folium.Marker([45.8234, 15.8678],popup='<strong>Location Two</strong>',
              tooltip=tooltip,icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([45.7434, 15.9678],popup='<strong>Location Three</strong>',
              tooltip=tooltip,icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([45.7834, 15.9978],popup='<strong>Location Four</strong>',
              tooltip=tooltip,icon=folium.Icon(color='green', icon='leaf')).add_to(m),
folium.Marker([45.7854, 15.8668],popup='<strong>Location Five</strong>',
              tooltip=tooltip,icon=logoIcon).add_to(m),
folium.Marker([45.7889, 15.8968],popup=folium.Popup(max_width=450)
              .add_child(folium.Vega(json.load(open(vis)),  width=450, height=250))).add_to(m)

# circle marker
folium.CircleMarker(
    location=[45.8899, 15.9988],
    radius=100,
    popup='My Random Place',
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)

#geojson overlay
folium.GeoJson(overlay, name='zagreb').add_to(m)

#generate map
m.save('map.html')

