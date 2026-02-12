
import random
import time

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
        self.stress_factor = 0
        self.glitch_factor = 0.2

    def talk(self, message):
        luck = random.random()
        if luck < self.glitch_factor or self.stress_factor > 50:
            print(f'[ROBOT]: {random.choice(excuses)}')
            return False
        else:
            print(f'[ROBOT]: {message}')
            return True

# Start Function
def start():


    def load():
        things = ['#', '!', '.', '@', '*', '?', '%']
        for i in range(20):
            thing = random.choice(things)
            print(thing, end='', flush=True)
            time.sleep(0.1)
            if random.random() < 0.1:
                time.sleep(0.1)
        print()
    bot = Robot()


    print('Connecting...')
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
    print('\nAnalysis in progress...')
    load()

    print('\n--ANALYSIS--')
    print('There are total of 4 cables scattered across a square object. It makes beep-boop sounds.')
    print('Oh! This is a bomb and the timer is started.')
    load()




    tasks = ['BOOM', 'NOTHING', 'NOTHING', 'SAFE']
    random.shuffle(tasks)

    cables = {
        'red_cable': Cable('Red', tasks[0]),
        'blue_cable': Cable('Blue', tasks[1]),
        'yellow_cable': Cable('Yellow', tasks[2]),
        'green_cable': Cable('Green', tasks[3])
    }

    def control(answer):
        if answer == 'BOOM':
            print('\n!!! BOOM !!!')
            print('System failure. Error 404')
            exit()
        elif answer == 'NOTHING':
            print('\n[NOTIFICATION]: Nothing happened. The ticking continues.')
        elif answer == 'SAFE':
            print('\n*** SAFE ***')
            print('The bomb has been defused.')
            exit()




# Main Loop
    while True:
        cmd = input('\nSYSTEM_ADMIN@ROOT:~$ ').strip().lower()
        bot.stress_factor += 10

        if cmd == 'red_cable.cut':
            if cables['red_cable'].was_cut == False:
                if bot.talk('Accessing Red Cable archives... Cutting now.'):
                    result = cables['red_cable'].cut()
                    control(result)
            else:
                print('It is already cutted, smart guy.')

        elif cmd == 'blue_cable.cut':
            if cables['blue_cable'].was_cut == False:
                if bot.talk('Initiating Blue Cable severance protocol.'):
                    result = cables['blue_cable'].cut()
                    control(result)
            else:
                print('It is already cutted, smart guy.')

        elif cmd == 'yellow_cable.cut':
            if cables['yellow_cable'].was_cut == False:
                if bot.talk('Yellow Cable selected. Hope you aren\'t colorblind.'):
                    result = cables['yellow_cable'].cut()
                    control(result)
            else:
                print('It is already cutted, smart guy.')

        elif cmd == 'green_cable.cut':
            if cables['green_cable'].was_cut == False:
                if bot.talk('Green Cable... Typical choice for the hopeful.'):
                    result = cables['green_cable'].cut()
                    control(result)
            else:
                print('It is already cutted, smart guy.')

        elif cmd == 'exit':
            break

        else:
            bot.talk(f'Syntax Error: \'{cmd}\' is not a valid command.')

start()


















