#!/usr/bin/env python3

import tkinter as tk
import sys
from ctext import Ctext

class TestApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title('Ctext test app')
        self.ctext = Ctext(self, background="black", foreground="white")
        self.ctext.pack(expand=True, fill='both')
        self.after_idle(self.create)

    def create(self):
        self.ctext.add_highlight_class('keyword', 'cyan', ['printf','return'])
        self.ctext.add_highlight_regexp('include', 'red', "<.*>")
        self.ctext.add_highlight_prefix('preprocessor', 'yellow', '#')
        self.ctext.add_highlight_chars('exclamation', 'magenta', '!')
        self.ctext.add_highlight_chars('punctuation', 'green', "\n\"\'")
        self.ctext.enable_c_comments(True)
        for line in (
                '/* this is a comment',
                ' */',
                '#include <stdio.h>',
                'int main(int argc, char *argv[])',
                '{',
                '    printf("Hello, World!\\n");',
                '    return 0;',
                '}'):
            self.ctext.insert('end', line, '', "\n", '')
        self.after_idle(self.rehighlight)
        self.after(2000, self.delete_class)
        self.after(5000, self.clearall)

    def delete_class(self):
        print("*** delete class")
        print(self.ctext.get_highlight_classes())
        self.ctext.delete_highlight_class('exclamation')
        print("'exclamation' class deleted.")
        print(self.ctext.get_highlight_classes())
        self.after_idle(self.rehighlight)

    def clearall(self):
        print("*** clearall")
        print(self.ctext.get_highlight_classes())
        self.ctext.clear_highlight_classes()
        print(self.ctext.get_highlight_classes())
        self.after_idle(self.rehighlight)

    def rehighlight(self):
        self.ctext.highlight('1.0', 'end - 1 line')


def main():
    """Program entry."""
    app = TestApp()
    app.mainloop()
    return 0

if __name__ == '__main__':
    sys.exit(main())
