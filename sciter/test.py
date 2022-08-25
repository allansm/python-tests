import sciter

class Frame(sciter.Window):
    def __init__(self):
        super().__init__(ismain=True, uni_theme=False, debug=False)
        self.set_dispatch_options(enable=True, require_attribute=False)
        pass

    def test(self):
        self.load_html(("<input type='button' style='width:100%;height:100%;font:20px' value='"+("helloworld "*3)+"' />").encode())

frame = Frame()
frame.load_file("index.html")
frame.run_app()
