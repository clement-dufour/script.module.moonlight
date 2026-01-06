import xbmc
import xbmcaddon
import subprocess

ADDON = xbmcaddon.Addon('script.module.moonlight')
ADDON_NAME = ADDON.getAddonInfo('name')

def log(text):
    message = f'{ADDON_NAME}: {text}'
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)
    return

def run():
    args = ['/usr/bin/systemctl', 'start', '--no-ask-password', '--no-block',
            'moonlight.service']
    return
