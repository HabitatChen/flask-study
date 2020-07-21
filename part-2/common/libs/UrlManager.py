from application import app
import os
import datetime

class UrlManager(object):
    @staticmethod
    def buildUrl( path ):
        path = '../../static' + path + '?ver=' + UrlManager.genReleaseVersion()
        return path

    @staticmethod
    def genReleaseVersion():
        ver = "%s" % ( UrlManager.getCurrentTime("%Y%m%d%H%M%S%f"))
        return ver

    def getCurrentTime(frm="%Y-%m-%d %H-%M-%S"):
        dt = datetime.datetime.now().__format__(frm)
        return dt




