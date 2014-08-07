WhereTheHellIsFios
==================

## A Scraper to grab Verizon FIOS data from one of their web APIs. Should be interesting to analyze.
###PSA: Wow that was fast. The API endpoint that the scraper called has been shut down. Less than 12 hours later. I didn't even get to send them a courtesy heads up (was going to but it was late, gotta sleep eventually).

### About
The exposed API call was in the mapping tool of a site called musthavefios.verizon.com and it accessed `http://musthavefios.verizon.com/scripts/data/fios_geo_data_compact_nyc.js` (using nyc as an example).

After looking through the XHR requests I found a bunch of other region data was sent to my browser for the following cities: albany, baltimore, boston, buffalo, centralpa, dallas, dc, harrisburg, la, nyc, palmsprings, philly, pittsburgh, providence, richmond, southva, sussex, syracuse, and tampa

The exact call was of the form: musthavefios.verizon.com/default.aspx?region=nyc

###Why/How?

So yeah. Last night I spoke with a lovely verizon rep (no, really she was extremely nice) with whom I was a little more curt than courtesy should allow. She informed me that the network was adding *no* new addresses "through 2015", now that phrasing is a bit ambiguous, but I took it as the worst meaning that I have 0 hope of having decent internet speeds until 2016, so I wanted to see where exactly I would have to move if I wanted faster internet and began looking through their marketing sites for detailed availability data. First I looked at the XHR data on their "Is FiOS available?" page. This turned out to be a dead end.

First candidate was `http://fios.verizon.com/availability_post4.php` which takes a POST and a param called `AvailabilityZipCode`, but it only tells you if the service is "available" in that zipcode, which doesn't tell you a while lot. I poked around for other potential params but unfortunately could find none.

Eventually I went to the WayBackMachine and looked at Verizon's old promotional websites for FIOS and found a bunch of good candidate API endpoints that were still alive. I forget where exactly I found the link to musthavefios.verizon.com, but I think it was in some sales-funnel thing on one of the wayback sites, and when I visisted it and the map popped up SPECIFIC addresses I was wicked psyched. Now next time I move I will be able to cross-reference by FIOS availability without having to use Verizon's awful address picker.
