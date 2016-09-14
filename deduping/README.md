# Deduping subdirectories and contents

 The script does the following:

 1. for subdirectories starting with specific url/text, gets oldest created directory
 2. copies the list of oldest unique subdirectories to new directory "<given_dest_path>/deduped_dirs"
 3. removes all subdirectories from the source path

 you just need to provide the src and dest arguments. (see options with ./deduping.py --help)

 Sample output (sample_deduping is source directory and deduped_dirs is the destination:

```
 payal@payal-ThinkPad-T520 ~/Documents $ mkdir www.aol.com_2015-04-02_10
 payal@payal-ThinkPad-T520 ~/Documents $ mkdir www.yahoo.com_2014-05-03
 payal@payal-ThinkPad-T520 ~/Documents $ mkdir www.google.com_2014-05-03
 payal@payal-ThinkPad-T520 ~/Documents $ mkdir www.aol.com_2015-04-02
 payal@payal-ThinkPad-T520 ~/Documents $ mkdir www.aol.com_2015-04-03
 payal@payal-ThinkPad-T520 ~/Documents $ mkdir www.yahoo.com_2014-05-04
 payal@payal-ThinkPad-T520 ~/Documents $ mkdir www.google.com_2014-05-04
 payal@payal-ThinkPad-T520 ~/Documents $ ./deduping.py
 Moving all oldest unique url directories to destination...
 Removing all subdirectories from source path...
 All done
 payal@payal-ThinkPad-T520 ~/Documents $ ls -l sample_deduping/
 total 0
 payal@payal-ThinkPad-T520 ~/Documents $ ls -l deduped_dirs/
 total 12
 drwxr-xr-x 3 payal payal 4096 Jan 16 21:40 www.aol.com_2015-04-02
 drwxr-xr-x 3 payal payal 4096 Jan 16 21:41 www.google.com_2014-05-03
 drwxr-xr-x 3 payal payal 4096 Jan 16 21:41 www.yahoo.com_2014-05-03
 ```
