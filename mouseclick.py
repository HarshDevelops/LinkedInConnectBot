from pynput.mouse import Listener

def on_right_click(x, y, button, pressed):
    if button == button.right and pressed:
        print(f"Mouse coordinates: x={x}, y={y}")

# Create a listener and register the callback function
with Listener(on_click=on_right_click) as listener:
    listener.join()
