
from pathlib import Path

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from ui.sidebar import Sidebar
from ui.pages.dashboard import DashboardPage
from ui.pages.placeholder import PlaceholderPage


class AegisSysWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AegisSys | Security Console")
        self.resize(1280, 800)
        self.setMinimumSize(1000, 650)

        self.page_widgets = {}

        self.setup_ui()
        self.load_theme()
        self.show_page("Dashboard")

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        root_layout = QHBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        self.sidebar = Sidebar()
        root_layout.addWidget(self.sidebar)

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 26, 30, 26)
        content_layout.setSpacing(22)

        self.page_title = QLabel("Dashboard")
        self.page_title.setObjectName("pageTitle")
        content_layout.addWidget(self.page_title)

        self.page_stack = QStackedWidget()
        content_layout.addWidget(self.page_stack, 1)

        root_layout.addWidget(content, 1)

        self.sidebar.page_selected.connect(self.show_page)

        for page_name in Sidebar.PAGES:
            if page_name == "Dashboard":
                page = DashboardPage()
            else:
                page = PlaceholderPage(page_name)

            self.page_widgets[page_name] = page
            self.page_stack.addWidget(page)

    def show_page(self, page_name):
        page = self.page_widgets.get(page_name)

        if page is None:
            return

        self.page_title.setText(page_name)
        self.page_stack.setCurrentWidget(page)

    def load_theme(self):
        theme_path = (
            Path(__file__).resolve().parents[1]
            / "styles"
            / "aegissys.qss"
        )

        if theme_path.exists():
            self.setStyleSheet(
                theme_path.read_text(encoding="utf-8")
            )
        else:
            print(f"Warning: Theme file not found: {theme_path}")
