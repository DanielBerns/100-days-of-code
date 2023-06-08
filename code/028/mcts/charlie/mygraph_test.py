from mygraph import Parser, Action, ActionContext, get_alphabet

class Save(Action):
    def __init__(self):
        super().__init__()
        
    def execute(self, 
                source: str, 
                context: ActionContext) -> None:
        super().execute()


def main():
    
    text = "This is a test"
    alphabet = get_alphabet(text)

    parser = Parser(alphabet)
    parser.update_actions_per_character('abcedfghijklmnopqrstuvwxyz', Save())
    print(parser.check())


if __name__ == '__main__':
    main()
