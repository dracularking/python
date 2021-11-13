from plyer import notification

# specify the parameters
title = 'Hello Amazing people!'

message = 'Thank you for reading! Take care!'

notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)
