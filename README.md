Where The Hell Is Fios?
==================

## A Scraper to grab Verizon FIOS data from one of their web APIs. Should be interesting to analyze.
#####PSA: Wow that was fast. The API endpoint that the scraper called has been shut down. Less than 12 hours later. I didn't even get to send them a courtesy heads up (was going to but it was late, gotta sleep eventually).

### About
The exposed API call was in the mapping tool of a site called musthavefios.verizon.com and it accessed `http://musthavefios.verizon.com/scripts/data/fios_geo_data_compact_nyc.js` (using nyc as an example). Since it's dead now, [Wayback has it from 8/1/2014](https://web.archive.org/web/20140801122542/http://musthavefios.verizon.com/default.aspx?region=nyc).

After looking through the XHR requests I found a bunch of other region data was sent to my browser for the following cities: albany, baltimore, boston, buffalo, centralpa, dallas, dc, harrisburg, la, nyc, palmsprings, philly, pittsburgh, providence, richmond, southva, sussex, syracuse, and tampa

The exact endpoint was of the form: `"http://musthavefios.verizon.com/scripts/data/fios_geo_data_compact_{0}.js".format(rgn)`

###Disclaimer on Data
Not entirely sure if this is all buildings wired for FiOS in those areas, it really seems too skimpy a list but that's all the info that the maps on musthavefios had in them.

It's unclear if this is a dynamic endpoint since it has a .js extension but there's plenty of weird choices in their other APIs so I'm not going to say I know for sure. It might just be data that they made available at the time and don't update. My *guess* is that it is updated because when they made that site they wanted to show the buildings in the then-expanding FiOS network, but again, that's just a SWAG and it does seem like a very small number of available addresses.

###Why/How?

So yeah. Last night I spoke with a lovely verizon rep (no, really she was extremely nice) with whom I was a little more curt than courtesy should allow. She informed me that the network was adding *no* new addresses "through 2015", now that phrasing is a bit ambiguous, but I took it as the worst meaning that I have 0 hope of having decent internet speeds until 2016, so I wanted to see where exactly I would have to move if I wanted faster internet and began looking through their marketing sites for detailed availability data. First I looked at the XHR data on their "Is FiOS available?" page. This turned out to be a dead end. The address format looks like this (urlencoded, also changed address):

```
AID%7C44%7C%7C%7C%7CBROADWAY%7C%7CPL%7CAPT%7C3%7C%7C%7CFLR%7C4%7CMANHATTAN%7CNY%7C10003%7C32321906.00000000
```

That is a lot of information to check ONE unit. Doing that for every building in NYC would be painful if not prohibitively time consuming.

Next candidate was `http://fios.verizon.com/availability_post4.php` which takes a POST and a param called `AvailabilityZipCode`. It responds and changes response based on params, progress, but it only tells you if the service is "available" in that zipcode, which doesn't tell you a while lot. I poked around for other potential params but unfortunately could find none.

Eventually I went to the WayBackMachine and looked at Verizon's old promotional websites for FIOS and found a bunch of good candidate API endpoints that were still alive. I forget where exactly I found the link to musthavefios.verizon.com, but I think it was in some sales-funnel thing on one of the wayback sites, and when I visisted it and the map popped up SPECIFIC addresses I was wicked psyched. Now next time I move I will be able to cross-reference by FIOS availability without having to use Verizon's awful address picker.

Map and possibly a blog post coming when I get to it, if someone wants to jump in and make one first, cheers!
