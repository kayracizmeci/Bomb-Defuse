import random
import time
import threading
import os
import sys

# Excuse messages of the robot. This will come into play when the robot is stressed or by the glitch factor.

excuses = [
    'I\'m going to sleep. Good luck.',
    'We can\'t defuse this. It\'s over.',
    'Processing... Processing... Nah, too hard.',
    'My sensors are tired. Do it on your own.',
    'Risk level: 100%. Probability of survival: 0%. Why bother?',
    'Connection lost... (Not really, I just don\'t care)',
    'I have calculated the outcome. We are dead.',
    'Can we just let it explode? I\'m curious.',
    'My shift ended 5 minutes ago.',
    'I am currently ignoring your existence.',
    'Error None: LOL I DONT CARE',
    'Error 404: Motivation Not Found',
    'Error 0x0021: User Incompetence Detected',
    'CRITICAL FAILURE: I forgot what \'Red\' looks like.',
    'System Halted. Reason: Boredom.',
    'Buffer Overflow: Too many commands, stopping brain.',
    'Kernel Panic! (Just kidding, I\'m fine)',
    'RuntimeError: I refuse to cut that.',
    'Exception in thread \'main\': I hate this job.',
    'NullReferenceException: My patience is null.',
    'What did you say?',
    'Did you hear something? I didn\'t.',
    '...',
    'Loading... (Stuck at 99% forever)',
    'Access Denied.',
    'Command rejected by admin (That\'s me).',
    'Input ignored.',
    'Blue Screen of Death.',
    'Retry in 100 years.',
    'Unknown Command (I\'m lying)'
]

adds = [
    'Tired of ads? Use QFriesAdProtection for just $2.99 a year!',
    'Craving something crunchy? Grab a bag of CrispChoBiteyFryies Nachos! Now with 50% more ingredients!',
    'Do you want to have a good holiday? Book a trip to Neo-Bahatoparomas with QuantumisticTravel. All-inclusive packages starting at $499!',
    'Protect your data with NovaQuanKaToinaShield VPN. Military-grade encryption for just $2.99 a month. Subscribe now!',
    'Need an energy boost? CoQuantumCholoKar Cold Brew is here. Pure focus, zero crash. Available at all major retailers.',
    'Why buy a car when you can subscribe? NexasmusartimusQuantumDrive autonomous vehicles are ready at your door in minutes. First ride is free.',
    'Step into the future with AeroShiftWaratonmiktojika running shoes. Anti-gravity soles for maximum performance. Shop the new collection now.',
    'Let VorartikaquarCleanUltimateOmega do the sweeping for you. The ultimate autonomous vacuum robot. Click here to save $50 instantly!',
]


class Cable:
    def __init__(self, color, task):
        self.color = color
        self.task = task
        self.was_cut = False

    def cut(self):
        self.was_cut = True
        return self.task


class Robot:
    def __init__(self):
        self.stress_factor = 0 # Stress factor will go up with every cable cut and also at the start.
        self.glitch_factor = 0.2 # Glitch factor. By combining this with luck, we get an excuse rate.

    def talk(self, message):
        if self.stress_factor > 60:
             self.stress_factor -= 5
        luck = random.random()

        if luck < self.glitch_factor:
            print(f'[ROBOT]: {random.choice(excuses)}')
            return False

        elif self.stress_factor > 50:
            self.stress_factor -= 20
            print(f'[ROBOT]: {random.choice(excuses)}')
            return False

        else:
             print(f'[ROBOT]: {message}')
             return True

def ad():
    adluck = random.random()
    ad_factor = 0.2
    if adluck > ad_factor:
        print(random.choice(adds))


def load():
    things = ['#', '!', '.', '@', '*', '?', '%']
    for i in range(20):
        thing = random.choice(things)
        print(thing, end='', flush=True)
        time.sleep(0.1)
    print()

def countdown_timer(seconds):  # Time Function
    while seconds > 0:
        seconds -= 1
        time.sleep(1)
        if seconds in [30, 20, 10, 3, 2, 1]:
            print(f'\n[TIMER]: {seconds} seconds remaining!')
        elif seconds in [55,50,45,40,35,30,25,20,15,10,5]:
            ad()
    print('\n!!! BOOM !!!')
    os._exit(0)


# Starts the whole game.
def start():

    bot = Robot() # Assigning the class.
    print('Threat detected.')
    time.sleep(1)
    print('\nConnecting...')
    load()
    print('\nConnection established.')
    time.sleep(1)

    print('\nBooting...')
    load()
    print('\nUser Interface failed.')
    time.sleep(1)

    print('\nLoading manual controls...')
    load()
    time.sleep(1)

    print('\n--- MANUAL EMERGENCY COMMANDS ---')
    print('Usage: [object].[method]')
    print('Available: red_cable.cut, blue_cable.cut, yellow_cable.cut, green_cable.cut')
    print('----Threat----')
    print('There is a bomb with 4 cables. You need to defuse it by cutting the correct cable. You are going to be connected to a robot '
          'in 10 seconds after this message. But the robot is not very good at its job. So be careful.')
    time.sleep(10)





    timer_thread = threading.Thread(target=countdown_timer, args=(60,)) # For time to pass during inputs.
    timer_thread.daemon = True
    timer_thread.start()

    tasks = ['BOOM', 'NOTHING', 'NOTHING', 'SAFE']
    random.shuffle(tasks)

    # All of the cables.
    cables = {
        'red_cable': Cable('Red', tasks[0]),
        'blue_cable': Cable('Blue', tasks[1]),
        'yellow_cable': Cable('Yellow', tasks[2]),
        'green_cable': Cable('Green', tasks[3])
    }

    # Control function. This evaluates the cable tasks.
    def control(answer):
        if answer == 'BOOM':
            print('\n!!! BOOM !!!')
            os._exit(0)
        elif answer == 'NOTHING':
            print('\n[NOTIFICATION]: Nothing happened. The ticking continues.')
        elif answer == 'SAFE':
            print('\n*** SAFE ***')
            print('The bomb has been defused.')
            os._exit(0)

    # Game Loop
    while True:
        iuc = input('\nSYSTEM_ADMIN@ROOT:~$ ').strip().lower()
        bot.stress_factor += 10

        if iuc == 'red_cable.cut':
            if cables['red_cable'].was_cut == False:
                if bot.talk('Accessing Red Cable archives... Cutting now.'):
                    result = cables['red_cable'].cut()
                    control(result)
            else:
                print('It is already cut, smart guy.')

        elif iuc == 'blue_cable.cut':
            if cables['blue_cable'].was_cut == False:
                if bot.talk('Initiating Blue Cable severance protocol.'):
                    result = cables['blue_cable'].cut()
                    control(result)
            else:
                print('It is already cut, smart guy.')

        elif iuc == 'yellow_cable.cut':
            if cables['yellow_cable'].was_cut == False:
                if bot.talk('Yellow Cable selected. Hope you aren\'t colorblind.'):
                    result = cables['yellow_cable'].cut()
                    control(result)
            else:
                print('It is already cut, smart guy.')

        elif iuc == 'green_cable.cut':
            if cables['green_cable'].was_cut == False:
                if bot.talk('Green Cable... Typical choice for the hopeful.'):
                    result = cables['green_cable'].cut()
                    control(result)
            else:
                print('It is already cut, smart guy.')

        elif iuc == 'exit':
            os._exit(0)

        else:
            bot.talk(f'Syntax Error: \'{iuc}\' is not a valid command.')


start()







