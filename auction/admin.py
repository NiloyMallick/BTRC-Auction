from cmath import phase

from django.contrib import admin

from auction.models import *

admin.site.register(Auction)
admin.site.register(Phase)
admin.site.register(Round)
admin.site.register(BidderInfo)
admin.site.register(AuctionDetails)

