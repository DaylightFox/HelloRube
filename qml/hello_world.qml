import QtQuick 2.0

Rectangle {
    id: page
    width: 320; height: 320 
    color: "lightgray"

    Text {
        id: helloText
        text: "Click Me"
        anchors.centerIn: page
        font.pointSize: 24; font.bold: true
    }

    MouseArea {
        anchors.fill: parent
        onClicked: console.log("Hello World !")
    }
}
