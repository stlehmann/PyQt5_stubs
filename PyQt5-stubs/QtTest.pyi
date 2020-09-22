# The PEP 484 type hints stub file for the QtTest module.
#
# Generated by SIP 5.4.0
#
# Copyright (c) 2020 Riverbank Computing Limited <info@riverbankcomputing.com>
#
# This file is part of PyQt5.
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
from PyQt5 import sip

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui  # add import of QtGui

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QAbstractItemModelTester(QtCore.QObject):

    class FailureReportingMode(int):
        QtTest = ... # type: 'QAbstractItemModelTester.FailureReportingMode'
        Warning = ... # type: 'QAbstractItemModelTester.FailureReportingMode'
        Fatal = ... # type: 'QAbstractItemModelTester.FailureReportingMode'

    @typing.overload
    def __init__(self, model: QtCore.QAbstractItemModel, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, model: QtCore.QAbstractItemModel, mode: 'QAbstractItemModelTester.FailureReportingMode', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def failureReportingMode(self) -> 'QAbstractItemModelTester.FailureReportingMode': ...
    def model(self) -> QtCore.QAbstractItemModel: ...


class QSignalSpy(QtCore.QObject):

    @typing.overload
    def __init__(self, signal: QtCore.pyqtBoundSignal) -> None: ...
    @typing.overload
    def __init__(self, obj: QtCore.QObject, signal: QtCore.QMetaMethod) -> None: ...

    def __delitem__(self, i: int) -> None: ...
    def __setitem__(self, i: int, value: typing.Iterable[typing.Any]) -> None: ...
    def __getitem__(self, i: int) -> typing.List[typing.Any]: ...
    def __len__(self) -> int: ...
    def wait(self, timeout: int = ...) -> bool: ...
    def signal(self) -> QtCore.QByteArray: ...
    def isValid(self) -> bool: ...


class QTest(sip.simplewrapper):

    class KeyAction(int): ...
    Press = ... # type: 'QTest.KeyAction'
    Release = ... # type: 'QTest.KeyAction'
    Click = ... # type: 'QTest.KeyAction'
    Shortcut = ... # type: 'QTest.KeyAction'

    class QTouchEventSequence(sip.simplewrapper):

        def __init__(self, a0: 'QTest.QTouchEventSequence') -> None: ...

        def commit(self, processEvents: bool = ...) -> None: ...
        def stationary(self, touchId: int) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def release(self, touchId: int, pt: QtCore.QPoint, window: typing.Optional[QtGui.QWindow] = ...) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def release(self, touchId: int, pt: QtCore.QPoint, widget: QtWidgets.QWidget) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def move(self, touchId: int, pt: QtCore.QPoint, window: typing.Optional[QtGui.QWindow] = ...) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def move(self, touchId: int, pt: QtCore.QPoint, widget: QtWidgets.QWidget) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def press(self, touchId: int, pt: QtCore.QPoint, window: typing.Optional[QtGui.QWindow] = ...) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def press(self, touchId: int, pt: QtCore.QPoint, widget: QtWidgets.QWidget) -> 'QTest.QTouchEventSequence': ...

    @typing.overload
    @staticmethod
    def touchEvent(widget: QtWidgets.QWidget, device: QtGui.QTouchDevice) -> 'QTest.QTouchEventSequence': ...
    @typing.overload
    @staticmethod
    def touchEvent(window: QtGui.QWindow, device: QtGui.QTouchDevice) -> 'QTest.QTouchEventSequence': ...
    @typing.overload
    @staticmethod
    def qWaitForWindowExposed(window: QtGui.QWindow, timeout: int = ...) -> bool: ...
    @typing.overload
    @staticmethod
    def qWaitForWindowExposed(widget: QtWidgets.QWidget, timeout: int = ...) -> bool: ...
    @typing.overload
    @staticmethod
    def qWaitForWindowActive(window: QtGui.QWindow, timeout: int = ...) -> bool: ...
    @typing.overload
    @staticmethod
    def qWaitForWindowActive(widget: QtWidgets.QWidget, timeout: int = ...) -> bool: ...
    @staticmethod
    def qWait(ms: int) -> None: ...
    @typing.overload
    @staticmethod
    def mouseRelease(widget: QtWidgets.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseRelease(window: QtGui.QWindow, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def mousePress(widget: QtWidgets.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def mousePress(window: QtGui.QWindow, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseMove(widget: QtWidgets.QWidget, pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseMove(window: QtGui.QWindow, pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseDClick(widget: QtWidgets.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseDClick(window: QtGui.QWindow, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseClick(widget: QtWidgets.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseClick(window: QtGui.QWindow, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keySequence(self, widget: QtWidgets.QWidget, keySequence: typing.Union[QtGui.QKeySequence, QtGui.QKeySequence.StandardKey, str, int]) -> None: ...
    @typing.overload
    def keySequence(self, window: QtGui.QWindow, keySequence: typing.Union[QtGui.QKeySequence, QtGui.QKeySequence.StandardKey, str, int]) -> None: ...
    @typing.overload
    @staticmethod
    def keySequence(widget: QtWidgets.QWidget, keySequence: typing.Union[QtGui.QKeySequence, QtGui.QKeySequence.StandardKey, str, int]) -> None: ...
    @typing.overload
    @staticmethod
    def keySequence(window: QtGui.QWindow, keySequence: typing.Union[QtGui.QKeySequence, QtGui.QKeySequence.StandardKey, str, int]) -> None: ...
    @typing.overload
    @staticmethod
    def keyRelease(widget: QtWidgets.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyRelease(widget: QtWidgets.QWidget, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...  # type: ignore
    @typing.overload
    @staticmethod
    def keyRelease(window: QtGui.QWindow, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyRelease(window: QtGui.QWindow, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...  # type: ignore
    @typing.overload
    @staticmethod
    def keyPress(widget: QtWidgets.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyPress(widget: QtWidgets.QWidget, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...  # type: ignore
    @typing.overload
    @staticmethod
    def keyPress(window: QtGui.QWindow, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyPress(window: QtGui.QWindow, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...  # type: ignore
    @typing.overload
    @staticmethod
    def keyEvent(action: 'QTest.KeyAction', widget: QtWidgets.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyEvent(action: 'QTest.KeyAction', widget: QtWidgets.QWidget, ascii: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyEvent(action: 'QTest.KeyAction', window: QtGui.QWindow, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyEvent(action: 'QTest.KeyAction', window: QtGui.QWindow, ascii: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @staticmethod
    def keyClicks(widget: QtWidgets.QWidget, sequence: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyClick(widget: QtWidgets.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyClick(widget: QtWidgets.QWidget, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...  # type: ignore
    @typing.overload
    @staticmethod
    def keyClick(window: QtGui.QWindow, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    @staticmethod
    def keyClick(window: QtGui.QWindow, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...  # type: ignore
    @staticmethod
    def qSleep(ms: int) -> None: ...
