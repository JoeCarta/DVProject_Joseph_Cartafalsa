## Decade in Planetary Astronomy

## Overview
#### Objective
My project will create a visualization that concurrently displays the extent of excellent conditions in telescope astronomy for 4 highly visible planets (Venus, Mars, Jupiter, Saturn) from NYC showing when positive factors overlap, with respect to time over the next 10 years.  This would help me and any viewer to digest multiple factors that attribute to clarity instead of thinking in abstract numbers and dates, and should also create something of a linear calendar for observing the planets used. 
#### Significance
This has personal significance to me as I enjoy trying to get better telescope observations of planets from home and have also come to be familiar with thee fact that excellent conditions come not just nightly (weather and atmosphere) but also cyclically and deterministically. In the latter case these are known years in advance, but many websites and applications with this information are nonvisual and/or outdated, and usually cover one planet at a time, so they don't fully show what I would find interesting to see.

One of my assignments for this class also partially inspired this larger visualization.
#### What are my aforementioned 'factors'?
I'm going to use opposition for outer planets and elongation for Venus (this is the main visual driver and most other factors will be predicated on this), then which oppositions bring us closer than others, then what season in NYC the opposition occurs and thus how high or sunken in the sky a planet can get at its peak, lastly I'm considering viewing angle for Saturn and thus how much of the rings' surface you can see from earth. 

Ideas that I dropped are lunar illumination and light pollution, moon visibility vs obscuring during optimal times, and some others

### Prior Work + Visualization Specifics

Looking through visualization types on D3 Graph Gallery, I decided to use a horizon chart or a modified ridgeline plot. What's useful about the horizon chart for my project is concurrently showing or comparing multiple distributions at once, I noticed this in the ridgeline example https://observablehq.com/@d3/ridgeline-plot, this example references and links to a horizon chart example which i find more appropriate https://observablehq.com/@d3/horizon-chart/2. but this example uses more rows than i would, and my peaks will likely be more cyclical or sinusoidal as viewing times come and go regularly every number of months. Each planet would get a row. Ridgelines generally use numerical distributions, in my project i plan on using this function not as a distribution, instead the y-axis height will show close approach to earth which will be smooth and repeating, or possible have y height reflect a sum of factors resulting in a higher total height. Either way, closer approaches relative to what that planet can do will display as higher peaks. For what season the opposition occurs in, I can either use winter/summer as a 2 category attribute and display that across the timeline using color or shading, or i can directly use closeness to zenith by week/month as a numerical and more precise way to show the benefit, and give this its own graph on the planet's row, or compound it into a singular height as mentioned. For Saturn ring visibility, I plan on using color, or size-dependent symbol plotting, to add the extra axis to Saturn's row

### Data
**Data Source**

I'll be pulling everything from NASA's JPL Horizons system ([https://ssd.jpl.nasa.gov/horizons/app.html#/](https://ssd.jpl.nasa.gov/horizons/app.html#/)), which is the canonical publicly available ephemeris service for solar system bodies and lets me query positions, distances, and other geometric quantities for any observer location and date range. To keep things scriptable I'll automate the queries through the Skyfield Python library, which wraps the same JPL ephemerides, and precompute one consolidated dataset for an NYC observer to feed into D3. Field documentation is at [https://ssd.jpl.nasa.gov/horizons/manual.html](https://ssd.jpl.nasa.gov/horizons/manual.html).

**Data Volume**

One row per planet per day across the 10-year window for the 4 planets gives roughly 14,600 rows and around 8 columns. Everything comes out of a single source so no merging or joining is needed.

**Data Richness**

The columns cover the inputs behind each of the factors I described earlier: geocentric distance from Earth (for opposition closeness), solar elongation (for opposition or greatest elongation timing), declination converted to maximum altitude during darkness from NYC (for the seasonal zenith factor), apparent magnitude (general brightness), and the saturnicentric latitude of Earth or B-angle, which is Saturn-specific and will be null for the other three planets. Date and planet name round out each row.
