import sys
import select
import argparse

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QAbstractItemView, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication, QCursor


def flush(list: QListWidget) -> None:
  for entry in [str(list.item(i).text()) for i in range(list.count()) if list.item(i).checkState() == Qt.Checked]:
    print(entry)
  sys.exit()

def center(window):
    screen = QGuiApplication.screenAt(QCursor().pos())
    fg = window.frameGeometry()
    fg.moveCenter(screen.geometry().center())
    window.move(fg.topLeft())

def main() -> None:
  if not select.select([sys.stdin,],[],[],0.0)[0]:
    raise Exception("You should really give this program some stdin...")

  # Argparse
  parser = argparse.ArgumentParser(
    # description=""
  )
  parser.add_argument("--name", type=str, nargs="+", help="Set the name the Window will display as")
  args = parser.parse_args()
  displayName = 'Reorder' if args.name == None else ' '.join(args.name)

  # Let's build this app shall we
  app = QApplication([])
  app.setApplicationName(displayName)
  app.setApplicationVersion("0.0.1")

  # Set the Layout
  window = QWidget()
  main_layout = QVBoxLayout()
  window.setLayout(main_layout)

  # Populate and Display the List
  the_list = QListWidget()
  the_list.setDragDropMode(QAbstractItemView.InternalMove)
  for item in map(lambda x: x.replace('\n', ''), sys.stdin.readlines()):
    lol = QListWidgetItem()
    lol.setText(item)
    lol.setCheckState(Qt.Checked)
    the_list.addItem(lol)
  main_layout.addWidget(the_list)

  # Also add a cheeky Confirm Button.
  the_button = QPushButton()
  the_button.setText("Confirm")
  the_button.clicked.connect(lambda :flush(the_list))
  main_layout.addWidget(the_button)

  # Execute the App
  center(window)
  window.show()
  app.exec()



if __name__ == "__main__":
  main()