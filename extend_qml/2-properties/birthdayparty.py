"""
Translation of the "Extending QML - Adding Types" example on the Qt reference website

http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-properties.html

BirthdayParty Implementation for Qml
http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-properties-birthdayparty-h.html
http://doc.qt.nokia.com/latest/declarative-cppextensions-referenceexamples-properties-birthdayparty-cpp.html

Translation Notes:

    there are methods and properties

    properties are declared by assigning them a type, a getter, and a setter


PySide. QObject
PySide. Property

Either you have to specify the underlying methods as const (in C++) or specify a signal handler.

const methods vs error warnings
    Not sure how to get a method to be "const" in python; it doesn't seem to have much meaning.
    Actually anything without a signal handler will be const: you need a signal handler to modify an object (or at least to signal to the display code that the object has been modified.)

unicode vs QString
    Instead of QString type (doesn't seem to be in the PySide packages) you use the unicode builtin

--------------------
Original Header File
--------------------
#ifndef BIRTHDAYPARTY_H
 #define BIRTHDAYPARTY_H

 #include <QObject>
 #include <QDeclarativeListProperty>
 #include "person.h"

 // ![0]
 class BirthdayParty : public QObject
 {
     Q_OBJECT
 // ![0]
 // ![1]
     Q_PROPERTY(Person *host READ host WRITE setHost)
 // ![1]
 // ![2]
     Q_PROPERTY(QDeclarativeListProperty<Person> guests READ guests)
 // ![2]
 // ![3]
 public:
     BirthdayParty(QObject *parent = 0);

     Person *host() const;
     void setHost(Person *);

     QDeclarativeListProperty<Person> guests();
     int guestCount() const;
     Person *guest(int) const;

 private:
     Person *m_host;
     QList<Person *> m_guests;
 };
 // ![3]

 #endif // BIRTHDAYPARTY_H

-------------------------
Original Class Definition
-------------------------
#include "birthdayparty.h"

 BirthdayParty::BirthdayParty(QObject *parent)
 : QObject(parent), m_host(0)
 {
 }

 // ![0]
 Person *BirthdayParty::host() const
 {
     return m_host;
 }

 void BirthdayParty::setHost(Person *c)
 {
     m_host = c;
 }

 QDeclarativeListProperty<Person> BirthdayParty::guests()
 {
     return QDeclarativeListProperty<Person>(this, m_guests);
 }

 int BirthdayParty::guestCount() const
 {
     return m_guests.count();
 }

 Person *BirthdayParty::guest(int index) const
 {
     return m_guests.at(index);
 }
 // ![0]

"""


#include <QObject>
from PySide.QtCore import QObject

#include <QDeclarativeListProperty>
from PySide.QtDeclarative import ListProperty

# There are a number of macros used in Qt that are replaced with classes in PySide
# Property is used instead of Q_PROPERTY
# Signal is required for WRITE methods, to alert other elements that the property has changed
from PySide.QtCore import Property
from PySide.QtCore import Signal

#include "person.h"
from person import Person

class BirthdayParty(QObject):
    """
    Use unicode instead of QString
    """

    # * birthdayparty.h *
    # private:
    #     Person *m_host;
    #     QList<Person *> m_guests;
    # * birthdayparty.cpp *

    #.h   BirthdayParty(QObject *parent = 0);
    #.cpp BirthdayParty::BirthdayParty(QObject *parent) : QObject(parent), m_host(0) {}
    def __init__(self, parent=None):
        # these are automatic constructors in C++
        # : QObject(parent), m_host(0)
        super(BirthdayParty, self).__init__(parent)
        # Person *m_host;
        # : QObject(parent), m_host(0)
        # None is the python keyword for a null object vs C++ using 0 to set a null pointer
        self._host = None
        # QList<Person *> m_guests;
        # PySide seems to replace QLists with its own native lists. (see QtCore/qlist_conversions.h)
        self._guests = []

    #.h   Person *host() const;
    #.cpp Person *BirthdayParty::host() const {return m_host;}
    def getHost(self):
        return self._host

    # to avoid namespace collision with the property, host -> setHost
    #.h   Person *host() const;
    #.cpp void BirthdayParty::setHost(Person *c) { m_host = c; }
    def setHost(self, c):
        self._host = c

    # Q_PROPERTY(Person *host READ host WRITE setHost)
    host = Property(Person, getHost, setHost)

    #.h   int guestCount() const;
    #.cpp int BirthdayParty::guestCount() const { return m_guests.count(); }
    def guestCount(self):
        return len(self._guests)

    #.h   Person *guest(int) const;
    #.cpp Person *BirthdayParty::guest(int index) const
    def guest(self, index):
        return self._guests[index]

    #.h   QDeclarativeListProperty<Person> guests();
    #.cpp QDeclarativeListProperty<Person> BirthdayParty::guests() {
    #         return QDeclarativeListProperty<Person>(this, m_guests); }
    # TODO figure out how to instantiate/return this correctly. Check out the
    # following for guidance.
    # http://developer.qt.nokia.com/doc/qt-4.8/qdeclarativelistproperty.html

    # guests -> getGuests (python doesn't support overloading functions/attributes)
    def getGuests(self):
        return self._guests

    # Q_PROPERTY(QDeclarativeListProperty<Person> guests READ guests)
    # guests -> getGuests (python doesn't support overloading functions/attributes)
    guests = ListProperty(Person, getGuests)
