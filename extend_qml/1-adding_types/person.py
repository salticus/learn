"""
Translation of the "Extending QML - Adding Types" example on the Qt reference website

http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-adding.html

Hopefully seeing the translation will:
    1. illustrate the patterns in the PySide wrappings so developers will be
    better able to adapt or use existing C++ examples
    2. Give a better feel for the environment and approach of Qt in general


Person Implementation for Qml

http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-adding.html

Translation Notes:

    there are methods and properties

    properties are declared by assigning them a type, a getter, and a setter


PySide. QObject
PySide. Property

Either you have to specify the underlying methods as const (in C++) or specify a signal handler.

const methods vs error warnings
    Not sure how to get a method to be "const" in python; it doesn't seem to have much meaning.
    Actually anything without a signal handler will be const.

unicode vs QString
    Instead of QString type (doesn't seem to be in the PySide packages) you use the unicode builtin

You know, all this boilerplate code just is asking for django-esque metaclass magic to take care of it.

--------------------
Original Header File
--------------------

 #ifndef PERSON_H
 #define PERSON_H

 #include <QObject>
 // ![0]
 class Person : public QObject
 {
     Q_OBJECT
     Q_PROPERTY(QString name READ name WRITE setName)
     Q_PROPERTY(int shoeSize READ shoeSize WRITE setShoeSize)
 public:
     Person(QObject *parent = 0);

     QString name() const;
     void setName(const QString &);

     int shoeSize() const;
     void setShoeSize(int);

 private:
     QString m_name;
     int m_shoeSize;
 };
 // ![0]

 #endif // PERSON_H

-------------------------
Original Class Definition
-------------------------
#include "person.h"

 // ![0]
 Person::Person(QObject *parent)
 : QObject(parent), m_shoeSize(0)
 {
 }

 QString Person::name() const
 {
     return m_name;
 }

 void Person::setName(const QString &n)
 {
     m_name = n;
 }

 int Person::shoeSize() const
 {
     return m_shoeSize;
 }

 void Person::setShoeSize(int s)
 {
     m_shoeSize = s;
 }

 // ![0]

"""

#include <QObject>
from PySide.QtCore import QObject

# There are a number of macros used in Qt that are replaced with classes in PySide
from PySide.QtCore import Property

class Person(QObject):
    """
        use unicode instead of QString
    """

    # * person.h *
    # private:
    #     QString m_name;
    #     int m_shoeSize;
    # * person.cpp *
    # Person::Person(QObject *parent) : QObject(parent), m_shoeSize(0)

    def __init__(self, parent=None):
        # these are automatic constructors in C++
        # : QObject(parent), m_shoeSize(0)
        super(Person, self).__init__(parent)
        # python convention is to use underscore to indicate private member variables
        self._shoeSize = 0
        self._name = "No Name Defined"

    def getShoeSize(self):
        return self._shoeSize

    def setShoeSize(self, value):
        self._shoeSize = value
        self.shoeSizeChanged.emit()

    # since this would clash with the property declaration, we change name --> getName
    # QString name() const;
    def getName(self):
        return self._name

    # void setName(const QString &);
    def setName(self, value):
        self._name = value

    name = Property(unicode, getName, setName)
    shoeSize = Property(int, getShoeSize, setShoeSize)
