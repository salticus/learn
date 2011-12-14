"""

PySide.QtGui . QApplication

Original Source: 
#include <QCoreApplication>
#include <QDeclarativeEngine>
#include <QDeclarativeComponent>
#include <QDebug>
#include "person.h"

 int main(int argc, char ** argv)
 {
     QCoreApplication app(argc, argv);
     qmlRegisterType<Person>("People", 1,0, "Person");

     QDeclarativeEngine engine;
     QDeclarativeComponent component(&engine, QUrl("qrc:example.qml"));
     Person *person = qobject_cast<Person *>(component.create());
     if (person) {
     qWarning() << "The person's name is" << person->name();
     qWarning() << "They wear a" << person->shoeSize() << "sized shoe";
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


# int main(int argc, char ** argv)
if __name__ == '__main__':
    # QCoreApplication app(argc, argv);
    app = QCoreApplication(sys.argv)

    # qmlRegisterType<Person>("People", 1,0, "Person");
    qmlRegisterType(Person, 'People', 1, 0, 'Person');

    # QDeclarativeEngine engine;
    engine = QDeclarativeEngine()

    # QDeclarativeComponent component(&engine, QUrl("qrc:example.qml"));
    component = QDeclarativeComponent(engine, QUrl("example.qml"))

    # Person *person = qobject_cast<Person *>(component.create());
    person = component.create()

    # if (person) {
    if person:
        # qWarning() << "The person's name is" << person->name();
        # qWarning() << "They wear a" << person->shoeSize() << "sized shoe";
        qWarning("The person's name is {p.name}".format(p=person))
        qWarning("They wear a {p.shoeSize} sized shoe".format(p=person))
    # } else {
    else:
        # qWarning() << component.errors();
        qWarning(component.errors())

    # return 0;
    # nothing equivalent here
