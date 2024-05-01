# Create a Widget class that can be cloned, including a unique
# serial number that should increment with each new clone to ensure each instance remains unique.






if __name__ == '__main__':
    widget_factory = WidgetFactory()
    widget1 = widget_factory.create_widget("WidgetA")
    print(widget1)  # WidgetA, Serial #1

    widget2 = widget_factory.clone_widget(widget1)
    print(widget2)  # WidgetA, Serial #2

    widget3 = widget_factory.clone_widget(widget1)
    print(widget3)  # WidgetA, Serial #3
