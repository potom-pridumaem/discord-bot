from interactions import Button, ButtonStyle


fuck_off = Button(
    style = ButtonStyle.SECONDARY,
    label = 'Отстань',
    emoji = "🤞",
    custom_id='butt' 
)

hello = Button(
    style = ButtonStyle.SUCCESS,
    label = 'Здарова',
    custom_id='butt2'
)

buttons = [fuck_off, hello]