import sys, fileinput
import select
import argparse

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QAbstractItemView, QPushButton

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
  for item in fileinput.input():
    lol = QListWidgetItem()
    lol.setText(item)
    lol.setCheckState(True)
    the_list.addItem(lol)
  main_layout.addWidget(the_list)

  # Also add a cheeky Confirm Button.
  the_button = QPushButton()
  the_button.setText("Confirm")
  main_layout.addWidget(the_button)

  # Execute the App
  window.show()
  app.exec()

main()

# TODO:
# setModal would be nice
# being centered at launch would be nice too