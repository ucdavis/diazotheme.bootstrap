""" Handles the top colored banner for each website"""

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from Acquisition import aq_inner

DEFAULT_WALL = '/++theme++diazotheme.bootstrap/images/banners/rec_blue_shadow.gif'

class BannerImage(BrowserView):
    
    def defaultWall(self):
        self.portal_state = getMultiAdapter((self.context, self.request),
            name=u"plone_portal_state")
        subsite = self.portal_state.navigation_root()
        defaultWall = getattr(aq_inner(subsite), 'default_wall', None)
        if defaultWall is None:
            defaultWall = DEFAULT_WALL
        return defaultWall
    
    
    def wallpaperURL(self):
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
       
        return portal_state.portal_url() + self.defaultWall()
        
    def __call__(self):
        context = self.context
        request = self.request
        portal_state = getMultiAdapter((context, request), name=u'plone_portal_state')
        self.request.response.redirect(portal_state.portal_url() + self.defaultWall())
        return