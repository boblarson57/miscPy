import os, shutil
from datetime import datetime
thisyr = 0
target = ''
targetYr = '2010'
rootdir = "d:\incomingppt"
siteDirs = os.listdir(rootdir)
for siteDir in siteDirs:
    print(siteDir)
    currSitePath = os.path.join(rootdir,siteDir)
    os.chdir(currSitePath)
    files = os.listdir(currSitePath)
    for file1 in files:
        print(file1)
        if os.path.isfile(file1):
            fn,ext = os.path.splitext(file1)
            ext = ext.lower()
            #if ext == '.xml':
            #    thisyr = file1[4:8]
            #    if thisyr == targetYr:
            #        target = os.path.join(currSitePath,targetYr)
            #        if os.path.exists(os.path.join(currSitePath,targetYr)) == False:
            #            os.makedirs(target)
            #        #shutil.move(file1,os.path.join(target,file1))
            if ext == '.dat' or ext == '.goes' or ext == '.xml' or ext == '.txt':
                #the yr is not in the filename, so use the modified date
                modDate = os.path.getctime(os.path.join(currSitePath,file1))
                fileYr = datetime.fromtimestamp(modDate).strftime('%Y')
                targetYr = fileYr
                #if str(fileYr) == targetYr:
                target = os.path.join(currSitePath,str(targetYr))
                if os.path.exists(os.path.join(currSitePath,str(targetYr))) == False:
                    os.makedirs(target)
                shutil.move(file1,os.path.join(target,file1))
                





