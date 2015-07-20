# Présentation #
TeleinfoFS permet d'accéder aux informations transmises par le compteur électrique (de type "bleu").

Ces informations sont présentées sous la forme d'un système de fichier virtuel actualisé en temps réel.

Exemple :
```
rb@linuxbox:~$ ~/devel/teleinfofs/teleinfofs.py /dev/ttyS0 /mnt/edf
rb@linuxbox:~$ ls -l /mnt/edf
total 0
-r--r--r-- 1 root root 12 2009-03-22 14:56 ADCO
-r--r--r-- 1 root root  9 2009-03-22 14:56 HCHC
-r--r--r-- 1 root root  9 2009-03-22 14:56 HCHP
-r--r--r-- 1 root root  1 2009-03-22 14:56 HHPHC
-r--r--r-- 1 root root  3 2009-03-22 14:56 IINST
-r--r--r-- 1 root root  3 2009-03-22 14:56 IMAX
-r--r--r-- 1 root root  2 2009-03-22 14:56 ISOUSC
-r--r--r-- 1 root root  6 2009-03-22 14:56 MOTDETAT
-r--r--r-- 1 root root  4 2009-03-22 14:56 OPTARIF
-r--r--r-- 1 root root  5 2009-03-22 14:56 PAPP
rb@linuxbox:~$ cat /mnt/edf/HCHP
020623502
```
# Téléchargement #
## [Télécharger TeleinfoFS 0.1.5](http://teleinfofs.googlecode.com/files/TeleinfoFS-0.1.5.tar.gz) ##



# Installation #
Tout d'abord, il vous faudra installer l'interpréteur Python et FUSE, dont dépend TeleinfoFS.

Debian/Ubuntu :
```
$ sudo apt-get install python fuse-utils libfuse2
```

Ensuite, [téléchargez](http://teleinfofs.googlecode.com/files/TeleinfoFS-0.1.5.tar.gz), décompactez et installez TeleinfoFS :
```
$ tar xzvf TeleinfoFS-0.1.5.tar.gz
$ cd TeleinfoFS-0.1.5
$ sudo python setup.py install
```
La bibliothèque [fusepy](http://code.google.com/p/fusepy/) est installée automatiquement.

Le système de fichier virtuel peut être monté grâce à la commande :
```
$ teleinfofs.py /dev/ttyS0 /mnt/teleinfo
```
où `/dev/ttyS0` est le nom du port série (si vous utilisez un convertisseur USB/série, ce sera probablement `/dev/ttyUSB0`) et `/mnt/teleinfo` le point de montage.
