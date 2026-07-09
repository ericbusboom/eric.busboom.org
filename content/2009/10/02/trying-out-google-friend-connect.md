---
title: "Trying Out Google and Facebook Friend Connect"
date: 2009-10-02T13:00:09+00:00
draft: false
categories: ["opinion", "Uncategorized"]
author: "eric"
---

Would you be my Friend? Here is Google's Friend Connect Widget: 

var skin = {}; skin['BORDER_COLOR'] = '#cccccc'; skin['ENDCAP_BG_COLOR'] = '#e0ecff'; skin['ENDCAP_TEXT_COLOR'] = '#333333'; skin['ENDCAP_LINK_COLOR'] = '#0000cc'; skin['ALTERNATE_BG_COLOR'] = '#ffffff'; skin['CONTENT_BG_COLOR'] = '#ffffff'; skin['CONTENT_LINK_COLOR'] = '#0000cc'; skin['CONTENT_TEXT_COLOR'] = '#333333'; skin['CONTENT_SECONDARY_LINK_COLOR'] = '#7777cc'; skin['CONTENT_SECONDARY_TEXT_COLOR'] = '#666666'; skin['CONTENT_HEADLINE_COLOR'] = '#333333'; skin['NUMBER_ROWS'] = '5'; google.friendconnect.container.setParentUrl('/' /* location of rpc_relay.html and canvas.html */); google.friendconnect.container.renderMembersGadget( { id: 'div-4019134814077193782', site: '18179748395891449876' }, skin); And Here is Facebook's. Facebook requires a lot more work, because you have to program in XFBML Your picture, if you are logged into facebook: Here are a bunch of your friends: 

var widget_div = document.getElementById("profile_pics"); FB.ensureInit(function () { FB.Facebook.get_sessionState().waitUntilReady(function() { FB.Facebook.apiClient.friends_get(null, function(result) { var markup = ""; var num_friends = result ? Math.min(10, result.length) : 0; if (num_friends > 0) { for (var i=0; i<num_friends; i++) { markup += ''; } } widget_div.innerHTML = markup; FB.XFBML.Host.parseDomElement(widget_div); }); }); });
