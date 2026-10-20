
import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import AegisSysWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("AegisSys")

    window = AegisSysWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
