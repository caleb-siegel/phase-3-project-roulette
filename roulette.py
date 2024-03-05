import random

class Board:
    betting_options = []
    def __init__(self, options, multiplier):
        self.options = options
        self.multiplier = multiplier
        self.set_betting_options()
    
    def set_betting_options(self):
        Board.betting_options.append(self)

numbers = Board(['0', '00', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'], 35)
colors = Board(['red', 'black'], 1)
evensodds = Board(['even', 'odd'], 1)
row_groups = Board(['1to12', '13to24', '25to36'], 2)
row_halves = Board(['1to18', '19to36'], 1)
columns = Board(['column1', 'column2', 'column3'], 2)

## use try/except for the bet_amount limiter
## limit amount of players



## Board Variables
green = ['0', '00']
red = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
black = ['2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28', '29', '31', '33', '35']
column1 = ['1', '4', '7', '10', '13', '16', '19', '22', '25', '28', '31', '34']
column2 = ['2', '5', '8', '11', '14', '17', '20', '23', '26', '29', '32', '35']
column3 = ['3', '6', '9', '12', '15', '18', '21', '24', '27', '30', '33', '36']

numbers = [green + red + black]

class Spin:
    def __init__(self, number):
        self.spin_result = []
        self.number = 0
        self.color = ''
        self.evensodds = ''
        self.column = ''
        self.row_group = ''
        self.row_halves = ''
        self.set_number_color(number)
        self.set_spin_color()
        self.set_spin_evensodds()
        self.set_spin_columns()
        self.set_spin_row_groups()
        self.set_spin_row_halves()
    
    def set_number_color(self, number):
        self.number = number[0][random.randint(0, len(number[0]) - 1)]
        self.spin_result.append(self.number)

    def set_spin_color(self):
        if self.number in green:
            self.color = 'green'
        elif self.number in red:
            self.color = 'red'
        else:
            self.color = 'black'
        self.spin_result.append(self.color)
    
    def set_spin_evensodds(self):
        if self.number == '0' or self.number == '00':
            self.evensodds = '0'
        elif int(self.number) % 2:
            self.evensodds = 'odd'
        else:
            self.evensodds = 'even'
        self.spin_result.append(self.evensodds)

    def set_spin_columns(self):
        if self.number == '0' or self.number == '00':
            self.column = ''
        elif self.number in column1:
            self.column = 'column1'
        elif self.number in column2:
            self.column = 'column2'
        else:
            self.column = 'column3'
        self.spin_result.append(self.column)

    def set_spin_row_groups(self):
        if int(self.number) < 13 and int(self.number) > 0:
            self.row_group = '1to12'
        elif int(self.number) < 25 and int(self.number) > 12:
            self.row_group = '13to24'
        elif int(self.number) < 37 and int(self.number) > 24:
            self.row_group = '25to36'
        self.spin_result.append(self.row_group)

    def set_spin_row_halves(self):
        if int(self.number) < 19 and int(self.number) > 0:
            self.row_halves = '1to18'
        elif int(self.number) < 37 and int(self.number) > 18:
            self.row_halves = '19to36'
        self.spin_result.append(self.row_halves)

class Player():
    
    def __init__(self, name):
        self.name = name
        self.pot = 0
        self.bet_amount = 0
        self.bet_location = ''
        self.result = ''
        self.decision = ''
        self.bet_amounts = []
        self.bet_locations = []
        self.playing = True
        self.betting = True
        self.decider = True

    def set_player_pot(self, pot):
        self.pot = pot

    def place_bet(self, location):
        if location == 'see bets':
            options = []
            for option in Board.betting_options:
                options.append(option.options)
            print(f"Here are the bets you can place: {options}")
            location = ''
        self.bet_location = location
        self.bet_amounts.append(self.bet_amount)
        self.bet_locations.append(location)

    @property
    def bet_amount(self):
        return self._bet_amount

    @bet_amount.setter
    def bet_amount(self, bet_amount):
        if bet_amount > self.pot:
            raise AttributeError(f'Cannot bet more than you have in the pot. Your pot is at {self.pot}')
        self._bet_amount = bet_amount

    # @property
    # def bet_location(self):
    #     return self._bet_location

    # @bet_location.setter
    # def bet_location(self, bet_location):
    #     options = []
    #     for option in Board.betting_options:
    #         options.append(option.options)
    #     if not bet_location in options:
    #         raise AttributeError('that is not a valid betting option')
    #     self._bet_location = bet_location

    def player_decision_keep_betting(self, decision):
        self.decision_keep_betting = decision

    def player_decision_end_game(self, decision):
        self.decision_end_game = decision

    def set_playing(self):
        self.playing = True
    
    def set_betting(self):
        self.betting = True

    def set_decider(self):
        self.decider = True


def start_game(players):
    # player buys in
    for key, player in players:
        pot_value = int(input(f'How much would you like to Buy-in {player.name}? '))
        player.set_player_pot(pot_value)

    playing = True
    while playing:

        # Determine Spin Results
        ball_spin = Spin(numbers)

        # player places bet(s)
        for key, player in players:
            player.set_betting()
            while player.betting:
                amount_ok = False
                while not amount_ok:
                    try:
                        amount = int(input(f'PLACE YOUR BETS: How much would you like to bet {player.name}? '))
                        player.bet_amount = amount
                        amount_ok = True
                    except AttributeError as e:
                        print(e)
                location = input(f'PLACE YOUR BETS: Where would you like to place your bet {player.name}? Enter "see bets" to see the betting options... ')
                player.place_bet(location)
                player.set_decider()
                while player.decider:
                    decision_bet = input(f'Would you like to place another bet {player.name}? yes or no... ')
                    player.player_decision_keep_betting(decision_bet)
                    if player.decision_keep_betting == 'no':
                        player.decider = False
                        player.betting = False
                    elif player.decision_keep_betting == 'yes':
                        player.decider = False
                    else:
                        print('That was not a valid entry. Try again')
                        
        for key, player in players:
            print(f"{player.name}'s bets are: {player.bet_locations}")

        print(f'SPIN RESULT: {ball_spin.spin_result}')

        # Determine if player won or lost
        for key, player in players:
            for i in range(len(player.bet_locations)):
                add_value = player.bet_amounts[i]
                if player.bet_locations[i] in ball_spin.spin_result:
                    for option in Board.betting_options:
                        if player.bet_locations[i] in option.options:
                            multiplier = option.multiplier
                    print(f'{player.name.upper()} WON THE BET!!! Add this value for bet {i + 1}: {add_value * multiplier}')
                    player.pot += add_value * multiplier
                    print(f"{player.name}'s pot is: {player.pot}")
                else:
                    print(f'{player.name} Lost :( . Remove this value for bet {i + 1}: {add_value}')
                    player.pot -= add_value
                    print(f"{player.name}'s pot is: {player.pot}")
            player.bet_amounts = []
            player.bet_locations = []
            multiplier = 0
        
        # Spin again
        if player.pot == 0:
            print(f'Game over')
            playing = False
        else:
            another_decider = True
            while another_decider:
                decision = input(f"Would you like to cash out? yes or no... ")
                if decision == 'yes':
                # player.player_decision_end_game(decision)
                    for key, player in players:
                        print(f"this is {player.name}'s winnings: ${player.pot}")
                    another_decider = False
                    playing = False
                elif decision == 'no':
                    another_decider = False
                else:
                    print('That was not a valid entry. Please try again.')
                    

# player(s) sits down
number_of_players = int(input("How many players are there? "))
players = {}

# Create instances of Player class based on the number of players
for i in range(1, number_of_players + 1):
    name = input(f"Enter the name of player {i}: ")
    players[f"player_{i}"] = Player(name)

# Starting the game
start_game(players.items())