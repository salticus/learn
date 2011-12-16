"""

PySide.QtGui .QApplication

Original Source:
#include <QCoreApplication>
#include <QDeclarativeEngine>
#include <QDeclarativeComponent>
#include <QDebug>
#include "birthdayparty.h"
#include "person.h"

int main(int argc, char ** argv)
{
 QCoreApplication app(argc, argv);

 qmlRegisterType<BirthdayParty>("People", 1,0, "BirthdayParty");
 qmlRegisterType<Person>("People", 1,0, "Person");

 QDeclarativeEngine engine;
 QDeclarativeComponent component(&engine, QUrl("qrc:example.qml"));
 BirthdayParty *party = qobject_cast<BirthdayParty *>(component.create());

 if (party && party->host()) {
     qWarning() << party->host()->name() << "is having a birthday!";
     qWarning() << "They are inviting:";
     for (int ii = 0; ii < party->guestCount(); ++ii)
         qWarning() << "   " << party->guest(ii)->name();
 } else {
     qWarning() << component.errors();
 }

 return 0;
}
"""

# not builtin like in C++
import sys

#include <QCoreApplication>
#include <QDeclarativeEngine>
#include <QDeclarativeComponent>
#include <QDebug>
from PySide.QtCore import QCoreApplication
from PySide.QtDeclarative import QDeclarativeEngine, QDeclarativeComponent, qmlRegisterType
from PySide.QtCore import qWarning, QUrl

#include "person.h"
from person import Person
#include "birthdayparty.h"
from birthdayparty import BirthdayParty


# int main(int argc, char ** argv)
if __name__ == '__main__':
    # QCoreApplication app(argc, argv);
    app = QCoreApplication(sys.argv)

    # qmlRegisterType<Person>("People", 1,0, "Person");
    qmlRegisterType(Person, 'People', 1, 0, 'Person');
    # qmlRegisterType<BirthdayParty>("People", 1,0, "BirthdayParty");
    qmlRegisterType(BirthdayParty, 'People', 1, 0, 'BirthdayParty');

    # QDeclarativeEngine engine;
    engine = QDeclarativeEngine()

    # QDeclarativeComponent component(&engine, QUrl("qrc:example.qml"));
    component = QDeclarativeComponent(engine, QUrl("example.qml"))

    # BirthdayParty *party = qobject_cast<BirthdayParty *>(component.create());
    party = component.create()

    # if (party && party->host()) {
    if party and party.host:
        # qWarning() << party->host()->name() << "is having a birthday!";
        # qWarning() << "They are inviting:";
        qWarning("{host.name} is having a birthday!".format(host=party.host))
        qWarning("They are inviting:")
        # for (int ii = 0; ii < party->guestCount(); ++ii)
            # qWarning() << "   " << party->guest(ii)->name();
        for x in range(party.guestCount()):
            qWarning("{}".format(party.guest(x)))
    # } else {
    else:
        # usual approach failed here: needed extract all the errors from a
        # list, and then cast them to strings.
        # trying to cast to unicode resulted in an incomplete error message
        for x in component.errors():
            qWarning(str(x))
        # qWarning() << component.errors();
        # qWarning(component.errors())

    # return 0;
    # nothing equivalent here
