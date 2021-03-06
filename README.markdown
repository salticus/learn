Small Examples
==============

extending_qml
-------------

NOTE: this has been stagnant for several years, with no definite plans to complete the exercise. But I keep it around in case I ever cross paths with pyside/qml development again.


Extending qml using PySide. Adapted from Nokia documentation on extending qml using C++. Based on tutorial at
http://doc.qt.nokia.com/latest/qml-extending.html

Two goals:

    1. Provide easily adaptable examples of qml extensions in Python.
    2. Provide examples of adapting C++ to PySide. Since C++ examples seem to be more plentiful than PySide examples, this may help Python developers learn to adapt C++ examples to PySide.

Also, gain a more fundamental understanding of Qt and Qml.

1-[adding_types](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-adding.html)

2-[properties](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-properties.html)

3-[coercion](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-coercion.html)

4.5-[methods](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-methods.html)

4-[default](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-default.html)

5-[grouped](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-grouped.html)

6-[attached](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-attached.html)

7-[signal](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-signal.html)

8-[valuesource](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-valuesource.html)

9-[binding](http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-binding.html)


Licensed under the GNU Free Documentation License, as original documentation falls under that license. Reference copy at http://www.gnu.org/licenses/fdl.html

Actually, each individual source snippet is prefixed with a BSD license. You work it out. This is mostly pedagogical in intent.

For reference, all code snippets should have the following prepended.

```
    /****************************************************************************
     **
     ** Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
     ** All rights reserved.
     ** Contact: Nokia Corporation (qt-info@nokia.com)
     **
     ** This file is part of the examples of the Qt Toolkit.
     **
     ** $QT_BEGIN_LICENSE:BSD$
     ** You may use this file under the terms of the BSD license as follows:
     **
     ** "Redistribution and use in source and binary forms, with or without
     ** modification, are permitted provided that the following conditions are
     ** met:
     **   * Redistributions of source code must retain the above copyright
     **     notice, this list of conditions and the following disclaimer.
     **   * Redistributions in binary form must reproduce the above copyright
     **     notice, this list of conditions and the following disclaimer in
     **     the documentation and/or other materials provided with the
     **     distribution.
     **   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
     **     the names of its contributors may be used to endorse or promote
     **     products derived from this software without specific prior written
     **     permission.
     **
     ** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
     ** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
     ** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
     ** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
     ** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
     ** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
     ** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
     ** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
     ** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
     ** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
     ** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
     ** $QT_END_LICENSE$
     **
     ****************************************************************************/
```
