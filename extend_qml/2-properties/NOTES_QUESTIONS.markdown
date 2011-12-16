Questions
=========

Does PySide use native python lists instead of QList?
    http://qt.gitorious.net/pyside/pyside/blobs/d2cd71313d0c44eaffe4b38ab3f9ac6daa2c20cb/PySide/QtCore/qlist_conversions.h
        Seems to indicate that Lists are used instead of QList in PySide: that QList objects are just converted over.
Difference between QDeclarativeListReference and QDeclarativeListProperty?
    reference vs property?

    PySide API 2 Removed QString, following PyQt4, 4.7
    http://www.pyside.org/docs/pyside/pysideapi2.html

Notes
=====

QDeclarativeListProperty
------------------------

Seems that PySide uses QtDeclarative.ListProperty instead of QDeclarativeListProperty

The only attributes currently supported are: type, append, at, clear, count

see the source:
    PySide/QtDeclarative/pysideqmlregistertype.cpp:175-196, 4e47b328 "Bumping to revision 1.0.9"
    gotten under  https://github.com/PySide/BuildScripts.git

a 2010 posting from the PySide site claims that QDeclarativeListProperty can be exposed, then points to an example that uses ListProperty(QDeclarativeItemSubClassFoo, appendMethod)


Troubleshooting
===============

glibc detected  * * * python: double free or corruption (fasttop): 0x0000000001999380
----------------------------------------------------------------------------------

Description: ran into this when tried running the main.py file. No diagnosis
yet. Following links shed light on the general class of error, but not on
specific problem spots with qt/qml.

Error replaced with another, after assigning the ListProperty in birthdayparty
to a specific name (rather than just instantiating it and throwing it away...
whoops). Also changed guests -> getGuests to avoid a namespace collision with
the property.


### [Common C reason for error](http://www.velocityreviews.com/forums/t629723-what-does-double-free-or-corruption-prev-mean-thank-u.html)

> Hey ~ everyone~
> What does this error mean?
>  * * * glibc detected  * * * double free or corruption (!prev):

The two common reasons for that error message are 1) passing the same
address to free twice and 2) overrunning an allocated area before
passing its address to free.

Chances are you do one or the other in the code you haven't shown us.
You need to provide a complete, compilable, and preferably short
example that demonstrates the undesirable behavior.

###  [NumPy: python sometimes not consistent across platforms](http://mail.scipy.org/pipermail/numpy-discussion/2008-April/032872.html) ###

> 1 items requested but only 0 read
> * * * glibc detected * * * /usr/bin/python: double free or corruption (fasttop):
> 0x08a5ac78  * * *
>
>
> but on my other machine it does it well and just answers...
>
> 1 items requested but only 0 read
> Out[102]:array([], dtype=int16)
>
> Any hint why this fails?

The problem is the behavior of realloc when size is 0 is not consistent across
platforms.  In the one case it does not free the original memory, but in the
other it frees the memory.


### [Redhat Bugzilla: Python 2.5 Malloc and Delete](https://bugzilla.redhat.com/show_bug.cgi?id=220923) ###

> Description of problem:
>
> This is a result of experiments with pungi-0.1.2-1.fc7. Repos used in this are
> two disk directories...  With 2097 packages in
> `/vols/l2/pungi/target/6.89/x86_64/os/Fedora the above writes 2097 lines in
> pkgorder-x86_64` and stops with
>
>  * * * glibc detected  * * * /usr/bin/python: double free or corruption (out):
> 0x00002aaaaaae8080  * * *
>
> Nothing happens after that and attaching 'strace' to a process shows
> that it stuck that way:
>
    $ strace -p 7945
    Process 7945 attached - interrupt to quit
    futex(0x3660947960, FUTEX_WAIT, 2, NULL
>
> until it is killed.

This is being caused by pyxf86config allocating memory with `PyObject_Malloc` and
then freeing it with `PyMem_DEL`.  In python 2.5, these actually have a
differences (so that the interpreter can return memory to the system).

