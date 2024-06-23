import flet as ft
from model import SmabLog


def create_header():
    headers = SmabLog().get_headers()
    return [ft.DataColumn(ft.Text(title, size=18, color="black", weight="bold")) for title in headers]


def create_row(data_list):
    data_cell = []
    for key in data_list.values():
        data_cell.append(ft.DataCell(ft.Text(key)))
    return data_cell


def create_values():
    values = SmabLog().get_table()
    data = [ft.DataRow(
        cells=create_row(el),
    ) for el in values]
    return data


def text_field():
    return ft.TextField(
        border_color="transparent",
        height=20,
        text_size=13,
        content_padding=0,
        cursor_color="black",
        cursor_width=1,
        cursor_height=18,
        color="black",
    )


# Define a method that creates and returns a textfield
def text_field_container(expand: bool | int, name: str, control: ft.TextField):
    return ft.Container(
        expand=expand,
        height=45,
        bgcolor="#ebebeb",
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(value=name, size=9, color="black", weight="bold"),
                control,
            ],
        ),
    )


form_style = {
    "border_radius": 20,
    "border": ft.border.all(1, "#ebebeb"),
    "bgcolor": "white10",
    "padding": 15,
}


class Form(ft.Container):
    def __init__(self):
        super().__init__(**form_style)
        # create a dt attribute
        # self.dt = dt

        self.row2_value = text_field()
        self.row3_value = text_field()

        # define and wrap each inside a container

        self.row2 = text_field_container(2, "Broker address", self.row2_value)
        self.row3 = text_field_container(1, "Topic name", self.row3_value)

        self.container = ft.Container(expand=True, height=45, width=300, bgcolor="transparent")

        # define a button to submit the data
        self.submit = ft.ElevatedButton(
            text="Connect",
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
            on_click=self.submit_data,
        )
        # compile all the attibutes into the class contianer
        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Row(controls=[self.row2, self.row3, self.container, self.submit], alignment="between"),
            ],
        )

    # define a method to submit data
    def submit_data(self, e: ft.TapEvent):
        # self.back.connect_client(address=self.row2_value.value, topic=self.row3_value.value)
        pass


class DataTable(ft.DataTable):
    def __init__(self):
        super().__init__()
        self.columns = create_header()
        self.rows = create_values()

    def fill_data_table(self, data, data_mqtt):
        # clear the data table rows for new/updated batch
        self.rows = []
        # check dict data type to understand following loop
        for values in self.df.values():
            # create a new DataRow
            data = ft.DataRow()
            data.cells = [
                ft.DataCell(ft.Text(value, color="black")) for value in values.values()
            ]

            self.rows.append(data)

        self.update()


def main(page: ft.Page):
    page.title = "MQTT Client Flet"
    page.bgcolor = "#fdfdfd"
    table = DataTable()
    form = Form()

    page.add(
        ft.Column(
            expand=True,
            controls=[
                form,
                ft.Divider(height=6, color="black"),
                ft.Row(
                    scroll=ft.ScrollMode.ADAPTIVE,
                    expand=True,
                    controls=[ft.Column(scroll=ft.ScrollMode.ADAPTIVE,
                                        controls=[table]), ],  # table ...
                ),
            ],
        )
    )

    page.update()
    # we can fill out the dt after we add the control to the page
    # table.fill_data_table()
