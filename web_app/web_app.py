"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# from rxconfig import config
from web_app import style
from web_app.state import State

# def index() -> rx.Component:
#     # Welcome Page (Index)
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", size="9"),
#             rx.text(
#                 "Get started by editing ",
#                 rx.code(f"{config.app_name}/{config.app_name}.py"),
#                 size="5",
#             ),
#             rx.link(
#                 rx.button("Check out our docs!"),
#                 href="https://reflex.dev/docs/getting-started/introduction/",
#                 is_external=True,
#             ),
#             spacing="5",
#             justify="center",
#             min_height="85vh",
#         ),
#         rx.logo(),
#     )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            style=style.input_style,
            on_change=State.set_question,  # set_question: built-in implicitly defined event handler
        ),
        rx.button(
            "Ask",
            style=style.button_style,
            on_click=State.answer,  # same for answer
            size="2",
        ),
    )


# Main index function to render the app
def index() -> rx.Component:
    return rx.container(
        rx.image(
            src="/NemetschekGroup_Black+Grey_Logo.png",  # must be placed in assets folder
            height="100px",
            alt="Company Logo",
            margin_bottom="3em",  # Increase this value for more space
        ),
        rx.color_mode.button(position="top-right"),
        # rx.heading("💬 Chat Assistant", size="7", margin_y="1em"),
        chat(),
        action_bar(),
        rx.button("Clear Chat", on_click=State.clear_history, size="1"),
        rx.text(
            "© 2025 Nemetschek SE. All rights reserved.",
            font_size="0.9em",
            color="#888",
            margin_top="3em",
            text_align="center",
        ),
        **style.app_bg_style,
    )


# ------------------
app = rx.App()
app.add_page(index, title="Chat Assistant", description="A simple chat assistant app.")
