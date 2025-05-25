# Style definitions for the web application.
app_bg_style = dict(bg="#eef0fa", min_height="100vh", padding_y="2em")

# --------------------------
# Styles for the chat messages.
# --------------------------
# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"

message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(bg="#F5EFFE", margin_left=chat_margin)
answer_style = message_style | dict(bg="#DEEAFD", margin_right=chat_margin)

# Styles for the action bar.
# --------------------------
# To change the font size in your text box, add a "font_size" property to input_style.
input_style = dict(
    border_width="1px", box_shadow=shadow, width="80%", height="2em", font_size="1.0em"
)
button_style = dict(bg="#81D8AE", box_shadow=shadow)
# button_style.update(dict(padding="0.75em 2em", font_size="1.1em"))
