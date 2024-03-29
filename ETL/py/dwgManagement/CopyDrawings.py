import os, sys, errno, shutil

folder = r'C:\Apps\Gizinta\gseFP\CADVault\Floorplans'
outfolder = r'C:\Apps\Gizinta\gseFP\CADVault\FloorplansTemp'

def main(argv = None):
    
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            bldg = dir[:4]
            try:
                site = lookup[bldg]
                sourceFolder = folder + '\\' + dir
                targetFolder = outfolder + '\\' + site + '\\'
                if not os.path.exists(targetFolder):
                    os.mkdir(targetFolder)
                targetFolder = outfolder + '\\' + site + '\\' + dir
                copytree(sourceFolder,targetFolder)
                print dir + ' copied'
            except:
                print dir + ' not found'
            
#print "processed " + str(len(dwgs)) + " drawings", str(dwgs)

def copytree(src, dst, symlinks=False, ignore=None):
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()
    try:
        os.makedirs(dst)
    except:
        pass
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                shutil.copytree(srcname, dstname, symlinks, ignore)
            else:
                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        #except Error as err:
        #    errors.extend(err.args[0])
    try:
        shutil.copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    #if errors:
    #    raise Error(errors)

lookup = {'1327':'UWS-UW Seattle'}


if __name__ == "__main__":
    main()
