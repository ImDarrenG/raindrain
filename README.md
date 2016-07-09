# raindrain
Script that downloads MetOffice rainfall radar scans

This is a quick and dirty script that, given your API key and a target path, will download UK rainfall radar images.

To use it, replace your API key, and if necessary, the value for data path, the directory where the images will be stored.

I use cron on a Pi to run the script every 15 minutes, which is the rate that new images are made available to the API.

### More info
For more information about the data/api see: http://www.metoffice.gov.uk/datapoint/product/rainfall-radar-map-layer

### Improvements
* Error handling
* The API endpoint exposes other data, download the other data, maybe determine which by looking at args
* Pass API key and data path in args rather than hardcoded
* Use the image format as the saved file extension
