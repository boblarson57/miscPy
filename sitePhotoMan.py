import os, shutil
from shutil import copyfile
from datetime import datetime
thisyr = 0
targetdir = "p:\\"
rootdir = 'p:\load'
siteDirs = os.listdir(rootdir)
for siteDir in siteDirs:
    if siteDir.find('-') > 0:
        delim = '-'
    elif siteDir.find('_') > 0:
        delim = '_'
    siteID,network = siteDir.split(delim)
    yrs = os.listdir(os.path.join(rootdir,siteDir))
    for yr in yrs:
        if yr > '2011':
            photos = os.listdir(os.path.join(rootdir,siteDir,yr))
            for photo in photos:
                if photo <> 'Thumbs.db': 
                    photoname,ext = os.path.splitext(photo)
                    nameparts = photoname.split('_')
                    photoType = nameparts[3]
                    dest =  os.path.join(targetdir,network,siteID,'sv'+yr,photo)
                    if os.path.exists(os.path.join(targetdir,network,siteID,'sv'+yr)) == False:
                         os.makedirs(os.path.join(targetdir,network,siteID,'sv'+yr))
                    copyfile(os.path.join(rootdir,siteDir,yr,photo),dest)
                    print(siteDir)

   
                





