#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import ConfigParser, os

config = ConfigParser.ConfigParser()
config.readfp(open('grabber.conf'))

api = twitter.Api(consumer_key=config.get("twitter", "consumer_key"),
    consumer_secret=config.get("twitter", "consumer_secret"),
    access_token_key=config.get("twitter", "access_token_key"),
    access_token_secret=config.get("twitter", "access_token_secret"))

statuses = api.GetSearch(term=["#kcandle"])

for s in reversed(statuses):
    # print s

    source = s.user.name

    target = ", ".join([ i.name for i in s.user_mentions if i.name != source ])
#    topics = " ".join([ "#"+h.text for h in s.hashtags if h.text.lower() != "kcandle"])
    topics = " ".join([ "#"+h.text for h in s.hashtags ])

    print  u"[%s] %s 🔥 → %s : %s"  % ( s.created_at, source, target, topics )
    print s.text
    print ""
