from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class Sidebar(QFrame):
    page_selected = Signal(str)

    PAGES = [
        "Dashboard",
        "Assistant",
        "Security Assessment",
        "Findings",
        "Remediation Center",
        "Action Approval",
        "Audit Log",
        "Reports",
        "System Information",
        "AI Status",
        "Settings",
    ]

    def __init__(self):
        super().__init__()
        self.setObjectName("sidebar")
        self.setFixedWidth(235)

        self.buttons = {}
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 24, 18, 20)
        layout.setSpacing(8)

        logo = QLabel("AEGISSYS")
        logo.setObjectName("logo")
        layout.addWidget(logo)

        subtitle = QLabel("LOCAL SECURITY PLATFORM")
        subtitle.setObjectName("muted")
        layout.addWidget(subtitle)

        layout.addSpacing(22)

        for page_name in self.PAGES:
            button = QPushButton(page_name)
            button.setObjectName("navButton")
            button.setCheckable(True)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(
                lambda checked=False, name=page_name: self.select_page(name)
            )

            self.buttons[page_name] = button
            layout.addWidget(button)

        layout.addStretch()

        status = QLabel("●  SYSTEM READY")
        status.setObjectName("status")
        layout.addWidget(status)

        self.select_page("Dashboard")

    def select_page(self, page_name):
        for name, button in self.buttons.items():
            button.setChecked(name == page_name)

        self.page_selected.emit(page_name)
