
import inquirer
questions = [
  inquirer.Text('name', message="What's your name"),
  inquirer.Text('surname', message="What's your surname"),
  inquirer.Text('phone', message="What's your phone number",
                validate=lambda x, _: re.match('\+?\d[\d ]+\d', x),
                )
]
answers = inquirer.prompt(questions)
