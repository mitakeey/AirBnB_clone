#!/usr/bin/python3
import cmd

class console(cmd.Cmd):
    '''simple command processor'''

    person = input('PLEASE IDENTIFY YOURSELF!!: ')
    intro = 'Identifying...\n ...\nWelcome to the HBNB shell {}. Type help or ? to list commands.\n' .format(person)
    prompt = '(hbnb) '
    tab = ['EOF', 'help', 'quit']


    def complete_foo(self, text, line, begidx, endidx):
        if not text:
            completions = self.tab
        else:
            completions = [f
                           for f in self.tab
                           if f.startswith(text)
                           ]
        return completions

    def do_EOF(self, line):
        ''' Command to interrupt prompt. EOF returns true which closes the prompt '''
        return True

    def do_quit(self, line):
        '''quit'''
        return True


if __name__ == '__main__':
    console().cmdloop()
