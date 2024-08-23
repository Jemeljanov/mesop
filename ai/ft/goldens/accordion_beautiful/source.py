import mesop as me

@me.stateclass
class State:
    open_section: str

def accordion_section(title: str, content: str):
    state = me.state(State)
    is_open = state.open_section == title

    with me.box(style=me.Style(
        border=me.Border.all(me.BorderSide(width=1, color=me.theme_var("outline"))),
        border_radius=4,
        margin=me.Margin(bottom=8)
    )):
        with me.box(style=me.Style(
            display="flex",
            justify_content="space-between",
            align_items="center",
            padding=me.Padding.all(12),
            background=me.theme_var("surface"),
            cursor="pointer"
        )):
            me.text(title, type="subtitle-1", style=me.Style(color=me.theme_var("on-surface")))
            me.button(
                "▼" if is_open else "▶",
                on_click=toggle_section(title),
                type="flat",
                style=me.Style(min_width=0, padding=me.Padding.all(4))
            )

        if is_open:
            with me.box(style=me.Style(
                padding=me.Padding.all(12),
                background=me.theme_var("surface-variant")
            )):
                me.text(content, style=me.Style(color=me.theme_var("on-surface-variant")))

@me.page()
def page():
    with me.box(style=me.Style(
        max_width=600,
        margin=me.Margin.symmetric(horizontal="auto"),
        padding=me.Padding.all(16)
    )):
        me.text("Accordion Example", type="headline-4", style=me.Style(
            color=me.theme_var("on-background"),
            margin=me.Margin(bottom=16)
        ))

        accordion_section("Section 1", "This is the content for section 1.")
        accordion_section("Section 2", "Here's some information for section 2.")
        accordion_section("Section 3", "And finally, the details for section 3.")